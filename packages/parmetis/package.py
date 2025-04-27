# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import sys

from spack.package import *


class Parmetis(CMakePackage):
    """ParMETIS is an MPI-based parallel library that implements a variety of
    algorithms for partitioning unstructured graphs, meshes, and for
    computing fill-reducing orderings of sparse matrices."""

    homepage = "http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview"
    url = "https://github.com/numpex/ParMETIS/archive/refs/tags/v4.0.4-rc.2.tar.gz"
    git = "https://github.com/numpex/ParMETIS"

    version("4.0.4-rc.2", sha256="dec52ed338c1a00202659e01aff0789d4509e0cc318d073015ea2a8a79629256")
#    version("4.0.3", sha256="f2d9a231b7cf97f1fee6e8c9663113ebf6c240d407d3c118c55b3633d6be6e5f")
#    version("4.0.2", sha256="5acbb700f457d3bda7d4bb944b559d7f21f075bb6fa4c33f42c261019ef2f0b2")

    variant("shared", default=True, description="Enables the build of shared libraries.")
    variant("gdb", default=False, description="Enables gdb support.")
    variant("int64", default=False, description="Sets the bit width of METIS's index type to 64.")
    variant("real64", default=False, description="Sets the bit width of METIS's real type to 64.")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@2.8:", type="build")
    depends_on("mpi")
    depends_on("metis@5:")
    depends_on("metis+int64", when="+int64")
    depends_on("metis~int64", when="~int64")
    depends_on("gklib", type=("build", "link", "run"))
    depends_on("metis+real64", when="+real64")
    depends_on("metis~real64", when="~real64")


    def cmake_args(self):
        spec = self.spec
        options = [
            self.define_from_variant("SHARED", "shared"),
            self.define_from_variant("GDB", "gdb"),
            self.define_from_variant("IDX64", "int64"),
            self.define_from_variant("REAL64", "real64"),
            self.define_from_variant("OPENMP", "omp"),
            self.define("CMAKE_C_COMPILER", spec["mpi"].mpicc),
            self.define("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx),
        ]

        if not "+shared" in spec:
            # Remove all RPATH options
            # (RPATHxxx options somehow trigger cmake to link dynamically)
            rpath_options = []
            for o in options:
                if o.find("RPATH") >= 0:
                    rpath_options.append(o)
            for o in rpath_options:
                options.remove(o)


        return options

    @run_after("install")
    def darwin_fix(self):
        # The shared library is not installed correctly on Darwin; fix this
        if (sys.platform == "darwin") and ("+shared" in self.spec):
            fix_darwin_install_name(prefix.lib)
