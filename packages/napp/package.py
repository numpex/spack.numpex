# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Napp(CMakePackage):
    """Named Arguments library for modern C++."""

    homepage = "https://github.com/vincentchabannes/napp"
    url = "https://github.com/vincentchabannes/napp/archive/refs/tags/v0.2.0.tar.gz"
    git = "https://github.com/feelpp/napp.git"

    maintainers("prudhomm", "vincentchabannes")

    license("LGPL-3.0-or-later", checked_by="prudhomm")

    version("master", branch="master")
    version("0.3.0", sha256="ccd75c32d89267cab14f3a10aeb9b7a34357ad9dc245ba15a293f2dad96af9c4")
    version("0.2.0", sha256="0316bfcd1be236d31f7fba4917ffa134db7a9e0f37f52c696b24e13c9f0ca6dd")
    version("0.1.0", sha256="254b455279b30cec8672e9faf6145c77fdcfb335e6003f4c7413305f663d1955")

    depends_on("cxx", type="build")

    def cmake_args(self):
        args = ["-DNAPP_ENABLE_TESTS=OFF", "-DNAPP_ENABLE_EXAMPLES=OFF", "-DNAPP_ENABLE_DOC=OFF"]
        return args
