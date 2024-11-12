# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Eigenrand(CMakePackage):
    """C++ Random Distribution Generator for Eigen."""

    homepage = "https://bab2min.github.io/eigenrand/"
    url = "https://github.com/bab2min/EigenRand/archive/refs/tags/v0.5.1.tar.gz"
    git = "https://github.com/bab2min/EigenRand.git"

    maintainers("prudhomm")

    license("MIT", checked_by="prudhomm")

    version("main", branch="main")
    version("0.5.1", sha256="105be932693c0f33398bbec8cd6342e86794d92dad9186d3c8ab46ea0140399f")

    patch("eigenrand-cmake.patch", when="@0.5.1:")

    depends_on("cxx", type="build")
    depends_on("eigen")

    def cmake_args(self):
        args = ["-DEIGENRAND_BUILD_TEST=OFF", "-DEIGENRAND_BUILD_BENCHMARK=OFF"]
        return args
