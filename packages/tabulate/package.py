# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Tabulate(CMakePackage):
    """tabulate is a header only Table Maker for Modern C++."""

    homepage = "https://github.com/p-ranav/tabulate"
    url = "https://github.com/p-ranav/tabulate/archive/refs/tags/v1.5.tar.gz"
    git = "https://github.com/p-ranav/tabulate.git"

    maintainers("prudhomm")

    license("MIT", checked_by="prudhomm")

    version("master", branch="master")
    version("1.5", sha256="16b289f46306283544bb593f4601e80d6ea51248fde52e910cc569ef08eba3fb")

    depends_on("cxx", type="build")
