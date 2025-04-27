# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gklib(CMakePackage):
    """A library of various helper routines and frameworks."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/numpex/GKlib.git"
    url = "https://github.com/numpex/GKlib/archive/refs/tags/v5.2.0-preview.1.tar.gz"
    git = "https://github.com/numpex/GKlib.git"

    maintainers("prudhomm")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("Apache-2.0")

    version("master", branch="master")
    version("5.2.0", sha256="f5cc0f4268c7a4e71a1d14f119d91c59a78663090fb30e0175406c91ca28b6df")

    variant("shared", default=True, description="Build shared library")
    variant("debug", default=False, description="Build with debug symbols")

    depends_on("c")
    
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_BUILD_TYPE", "debug"),
        ]
        return args
