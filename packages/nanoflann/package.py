# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Nanoflann(CMakePackage):
    """a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees."""

    homepage = "https://github.com/jlblancoc/nanoflann"
    url = "https://github.com/jlblancoc/nanoflann/archive/v1.2.3.tar.gz"

    license("BSD-2-Clause")

    version("1.6.2", sha256="c1b8f2e4d32c040249dad14a89dd03c5106a8c56f3e9ca4e60a0836a59259c0c")
    version("1.6.1", sha256="e258d6fd6ad18e1809fa9c081553e78036fd6e7b418d3762875c2c5a015dd431")
    version("1.6.0", sha256="f889026fbcb241e1e9d71bab5dfb9cc35775bf18a6466a283e2cbcd60edb2705")
    version("1.5.5", sha256="fd28045eabaf0e7f12236092f80905a1750e0e6b580bb40eadd64dc4f75d641d")
    version("1.5.4", sha256="a7f64d0bdff42614c561e52680b16de46c0edac9719f21f935c5e1f8b0654afc")
    version("1.4.3", sha256="cbcecf22bec528a8673a113ee9b0e134f91f1f96be57e913fa1f74e98e4449fa")
    version("1.2.3", sha256="5ef4dfb23872379fe9eb306aabd19c9df4cae852b72a923af01aea5e8d7a59c3")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def patch(self):
        filter_file("-mtune=native", "", "CMakeLists.txt")

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS=ON"]
        return args
