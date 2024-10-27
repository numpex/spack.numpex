# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Feelpp(CMakePackage, CudaPackage, ROCmPackage):
    """
    Feel++ is an Open-Source C++ library designed to solve a wide range of
    partial differential equations (PDEs) using advanced Galerkin methods.
    These methods include the finite element method (FEM), spectral element
    method, discontinuous Galerkin methods, and reduced basis methods.

    Feel++ is optimized for high-performance computing, enabling seamless
    parallel computing on large-scale systems, ranging from desktop machines
    to supercomputers with tens of thousands of cores. The library supports
    multi-physics simulations and provides a modular structure to simplify
    the development of applications.
    """

    homepage = "https://docs.feelpp.org"
    url = "https://github.com/feelpp/feelpp/archive/v0.110.2.tar.gz"
    git = "https://github.com/feelpp/feelpp.git"

    maintainers("prudhomm", "vincentchabannes")

    license("LGPL-3.0-or-later AND GPL-3.0-or-later")

    version("develop", branch="develop")
    version("preset", branch="2284-add-spack-environment-to-the-main-ci")

    # Define variants
    variant("toolboxes", default=True, description="Enable the Feel++ toolboxes")
    variant("mor", default=True, description="Enable Model Order Reduction (MOR)")
    variant("python", default=True, description="Enable Python wrappers")
    variant("quickstart", default=True, description="Enable the quickstart examples")
    variant("tests", default=False, description="Enable the tests")
    # Add variants for C++ standards
    variant(
        "cxxstd", default="20", description="C++ standard", values=["17", "20", "23"], multi=False
    )
    variant("kokkos", default=True, description="Enable Kokkos support")
    conflicts("^openmpi~cuda", when="+cuda")  # +cuda requires CUDA enabled OpenMPI
    # Specify dependencies with required versions
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.21:", type="build")
    depends_on("llvm@14.0.0:")
    depends_on("mpi")
    depends_on(
        "boost@1.75: +regex+date_time+filesystem+iostreams+mpi+multithreaded+program_options+serialization+shared+system+test"
    )
    depends_on("petsc@3.20 +mumps+hwloc+ptscotch +suite-sparse+hdf5 +hypre+kokkos")
    depends_on("slepc")
    depends_on("fmt")
    depends_on("cln")
    depends_on("eigen")
    depends_on("fftw")
    depends_on("libunwind")
    depends_on("libzip")
    depends_on("bison")
    depends_on("flex")
    depends_on("pugixml")
    depends_on("readline")
    depends_on("gsl")
    depends_on("glpk")
    depends_on("gl2ps")
    depends_on("ruby")
    depends_on("gmsh +opencascade+mmg+fltk")
    depends_on("curl")
    depends_on("glog")
    depends_on("gflags")
    depends_on("kokkos +threads+hwloc", when="+kokkos")
    depends_on("kokkos-kernels", when="+kokkos")

    for cuda_arch in CudaPackage.cuda_arch_values:
        depends_on(
            "kokkos +threads+hwloc+cuda+cuda_lambda cuda_arch=%s" % cuda_arch,
            when="+kokkos +cuda cuda_arch=%s" % cuda_arch,
        )
        depends_on(
            "kokkos-kernels+cuda cuda_arch=%s" % cuda_arch,
            when="+kokkos +cuda cuda_arch=%s" % cuda_arch,
        )
    for rocm_arch in ROCmPackage.amdgpu_targets:
        depends_on(
            "kokkos +threads+hwloc+rocm amdgpu_target=%s" % rocm_arch,
            when="+kokkos +rocm amdgpu_target=%s" % rocm_arch,
        )
    # Add dependencies for GPU support on AMD
    depends_on("hip", when="+rocm")

    with when("+rocm"):
        depends_on("hipblas")
        depends_on("hipsparse")
        depends_on("hipsolver")
        depends_on("rocsparse")
        depends_on("rocsolver")
        depends_on("rocblas")
        depends_on("rocrand")
        depends_on("rocthrust")
        depends_on("rocprim")

    # Python dependencies if +python variant is enabled
    depends_on("py-pytest", when="+python")
    depends_on("py-pandas", when="+python")
    depends_on("py-petsc4py", when="+python")
    depends_on("py-slepc4py", when="+python")
    depends_on("py-numpy", when="+python")
    depends_on("py-pybind11", when="+python")
    depends_on("py-sympy", when="+python")
    depends_on("py-plotly", when="+python")
    depends_on("py-scipy", when="+python")
    depends_on("py-tabulate", when="+python")
    depends_on("py-ipykernel", when="+python")
    depends_on("py-mpi4py", when="+python")
    depends_on("py-tqdm", when="+python")
    depends_on("python@3.7:3.11", when="+python", type=("build", "run"))

    def get_preset_name(self):
        spec = self.spec
        cpp_version = spec.variants["cxxstd"].value
        gpu="rocm" if "+rocm" in spec else "cpu"
        preset_name = f"feelpp-clang-cpp{cpp_version}-spack-{gpu}-release"
        return preset_name

    def cmake_args(self):
        """Define the CMake preset and CMake options based on variants."""
        args = [
            f"--preset={self.get_preset_name()}",
            self.define_from_variant("FEELPP_ENABLE_QUICKSTART", "quickstart"),
            self.define_from_variant("FEELPP_ENABLE_TESTS", "tests"),
            self.define_from_variant("FEELPP_ENABLE_TOOLBOXES", "toolboxes"),
            self.define_from_variant("FEELPP_ENABLE_MOR", "mor"),
            self.define_from_variant("FEELPP_ENABLE_FEELPP_PYTHON", "python"),
        ]
        if "+cuda" in self.spec:
            if not self.spec.satisfies("cuda_arch=none"):
                cuda_arch = self.spec.variants["cuda_arch"].value
                if self.spec.satisfies("@3.14:"):
                    args.append("--with-cuda-gencodearch={0}".format(cuda_arch[0]))
                else:
                    args.append(
                        "CUDAFLAGS=-gencode arch=compute_{0},code=sm_{0}".format(cuda_arch[0])
                    )
        # Handle ROCm support
        if '+rocm' in self.spec:
            # Set architecture
            if not self.spec.satisfies("amdgpu_target=none"):
                hip_arch = self.spec.variants['amdgpu_target'].value
                args.append(f"-DAMDGPU_TARGET={hip_arch[0]}")

            # Collect HIP include directories and libraries
            hip_pkgs = ['hipsparse', 'hipblas', 'hipsolver', 'rocsparse', 'rocsolver', 'rocblas']
            hip_ipkgs = hip_pkgs + ['rocthrust', 'rocprim']
            hip_lpkgs = hip_pkgs

            # Handle rocrand versioning
            if self.spec.satisfies("^rocrand@5.1:"):
                hip_ipkgs.append('rocrand')
            else:
                hip_lpkgs.append('rocrand')

            # Collect include and library flags
            hip_inc_flags = ' '.join([self.spec[pkg].headers.include_flags for pkg in hip_ipkgs])
            hip_lib_flags = ' '.join([self.spec[pkg].libs.joined() for pkg in hip_lpkgs])

            # Add HIP flags to CMake arguments
            args.append(f"-DHIP_INCLUDE_DIRS={hip_inc_flags}")
            args.append(f"-DHIP_LIBRARIES={hip_lib_flags}")
            args.append(f"-DHIP_LIBRARY_DIRS={self.spec['hip'].prefix}/lib -lamdhip64")
        return args

    def build(self, spec, prefix):
        cmake = which("cmake")
        cmake("--build", "--preset", self.get_preset_name())

    def install(self, spec, prefix):
        cmake = which("cmake")
        cmake("--build", "--preset", self.get_preset_name(), "-t", "install")

    def test(self, spec, prefix):
        ctest = which("ctest")
        ctest("--preset", self.get_preset_name(), "-R", "qs_laplacian")

    def setup_run_environment(self, env):
        import os
        env.set("FEELPP_DIR", self.prefix )
        env.prepend_path(
            "PYTHONPATH",
            os.path.join(
                self.spec.prefix.lib,
                "python{0}".format(self.spec["python"].version.up_to(2)),
                "site-packages",
            ),
        )
    def setup_dependent_build_environment(self, env, dependent_spec):
        """set FEELPP_DIR"""
        env.set("FEELPP_DIR", self.prefix )