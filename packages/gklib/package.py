# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gklib(CMakePackage):
    """A library of various helper routines and frameworks."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/feelpp/GKlib.git"
    url = "https://github.com/feelpp/GKlib/archive/refs/tags/v5.2.0-preview.1.tar.gz"
    git = "https://github.com/feelpp/GKlib.git"

    maintainers("prudhomm")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("Apache-2.0")

    version("master", branch="master")
    version("5.2.0", sha256="f5cc0f4268c7a4e71a1d14f119d91c59a78663090fb30e0175406c91ca28b6df")
    version("5.2.0-preview.3", sha256="463ca36bcc71d9ab4dcc98e11aa5cb74f8f64433adc8203afacc475239ee299f")
    version("5.2.0-preview.2", sha256="d4f77483fcd79fdf8f82a59335494073cf674b0625d66e87082b98edca8b19d9")
    version("5.2.0-preview.1", sha256="3bd8745e38dd9f0f095d7d5042d30f5cbdfb523519b447a962fe1e750ac8fa46")

    variant("shared", default=True, description="Build shared library")
    variant("debug", default=False, description="Build with debug symbols")

    depends_on("c")
    
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_BUILD_TYPE", "debug"),
        ]
        return args
