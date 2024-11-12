# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install indicators
#
# You can edit this file again by typing:
#
#     spack edit indicators
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Indicators(CMakePackage):
    """Activity Indicators for Modern C++"""

    homepage = "https://github.com/p-ranav/indicators"
    url = "https://github.com/p-ranav/indicators/archive/refs/tags/v2.3.tar.gz"
    git = "https://github.com/p-ranav/indicators.git"

    maintainers("prudhomm")

    license("MIT", checked_by="prudhomm")

    version("master", branch="master")
    version("2.3", sha256="70da7a693ff7a6a283850ab6d62acf628eea17d386488af8918576d0760aef7b")

    depends_on("cxx", type="build")
