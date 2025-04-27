# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Bvh(CMakePackage):
    """This library is a small, standalone library for BVH construction and traversal."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/feelpp/bvh.git"
    url = "https://github.com/feelpp/bvh.git"
    git = "https://github.com/feelpp/bvh.git"

    maintainers("prudhomm")

    license("MIT")

    version("master", branch="master")
    version("feelpp", branch="feelpp", preferred=True)

    depends_on("c")
    depends_on("cxx")
