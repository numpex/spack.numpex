# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Matplotplusplus(CMakePackage):
    """A C++ Graphics Library for Data Visualization.
    Modern C++ is being used for a variety of scientific applications, and this environment can benefit considerably from graphics libraries that attend the typical design goals toward scientific data visualization.
    """

    homepage = "https://alandefreitas.github.io/matplotplusplus/"
    url = "https://github.com/alandefreitas/matplotplusplus/archive/refs/tags/v1.2.1.tar.gz"
    git = "https://github.com/alandefreitas/matplotplusplus.git"

    maintainers("prudhomm")
    license("MIT", checked_by="prudhomm")

    version("master", branch="master")
    version("1.2.1", sha256="9dd7cc92b2425148f50329f5a3bf95f9774ac807657838972d35334b5ff7cb87")
    version("1.2.0", sha256="42e24edf717741fcc721242aaa1fdb44e510fbdce4032cdb101c2258761b2554")
    version("1.1.0", sha256="5c3a1bdfee12f5c11fd194361040fe4760f57e334523ac125ec22b2cb03f27bb")

    variant("pic", default=True, description="Position independent code")
    variant("shared", default=True, description="Build shared library")
    variant("opencv", default=False, description="Enable OpenCV support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("jpeg")
    depends_on("libpng")
    depends_on("zlib")
    depends_on("libtiff")
    depends_on("lapack")
    depends_on("fftw")
    depends_on("opencv", when="+opencv")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
        ]
        return args
