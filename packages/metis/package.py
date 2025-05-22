# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
import sys

from spack_repo.builtin.build_systems import cmake
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Metis(CMakePackage):
    """METIS is a set of serial programs for partitioning graphs, partitioning
    finite element meshes, and producing fill reducing orderings for sparse
    matrices.

    The algorithms implemented in METIS are based on the multilevel
    recursive-bisection, multilevel k-way, and multi-constraint partitioning schemes.
    """

    homepage = "http://glaros.dtc.umn.edu/gkhome/metis/metis/overview"
    url = "https://github.com/numpex/metis/archive/refs/tags/v5.3.0-rc.1.tar.gz"
    git = "https://github.com/numpex/metis.git"

    # not a metis developer, just package reviewer!
    maintainers("prudhomm")

    license("Apache-2.0")

    version("5.3.1-rc.6", sha256="6f4998f6a97b2cce566372f193a21a20dc578d381aae9d3070e33412bdadbb79", preferred=True)
    version("5.3.1-rc.3", sha256="325866e8d3687be8c487eeaa4b97971d1b3ed708d08af1ed748d46941c11a2ea")
    version("5.3.1-rc.2", sha256="c99d7ab05d527f96fe192ecda4929dc9d811e93107c43d9bbcde4cddf1cc3092")
    version("5.3.1-rc.1", sha256="4aa90f641e78bb30a684d15b7e38dd70a6ada191b623db4b7a1585deb9fe3432")
    version("5.3.0-rc.1", sha256="df4c6ec73f2c2d1e328ed2c43f00525cb6a2cd623e4a39727f36c3af7b7356ca")


    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gklib", type=("build","link","run"))
    variant(
        "no_warning",
        default=False,
        description="Disable failed partition warning print on all ranks",
    )
    variant("shared", default=True, description="Build shared libraries")

    variant("gdb", default=False, description="Enable gdb support")
    variant("int64", default=False, description="Use index type of 64 bit")
    variant("real64", default=False, description="Use real type of 64 bit")
    variant("omp", default=False, description="Enable OpenMP support")




class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        options = [
            self.define_from_variant("SHARED", "shared"),
            self.define_from_variant("GDB", "gdb"),
            self.define_from_variant("IDX64", "int64"),
            self.define_from_variant("REAL64", "real64"),
            self.define_from_variant("OPENMP", "omp"),
        ]

        if self.spec.satisfies("~shared"):
            # Remove all RPATH options
            # (RPATHxxx options somehow trigger cmake to link dynamically)
            rpath_options = []
            for o in options:
                if o.find("RPATH") >= 0:
                    rpath_options.append(o)
            for o in rpath_options:
                options.remove(o)

        return options

