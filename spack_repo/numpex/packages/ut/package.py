# Copyright Spack Project Developers. See COPYRIGHT file for details.
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
#     spack install ut
#
# You can edit this file again by typing:
#
#     spack edit ut
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Ut(CMakePackage):
    """C++20 μ(micro)/Unit Testing framework."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/boost-ext/ut/archive/refs/tags/v2.3.1.tar.gz"

    maintainers("prudhomm")

    license("UNKNOWN", checked_by="github_user1")

    version("2.3.1", sha256="e51bf1873705819730c3f9d2d397268d1c26128565478e2e65b7d0abb45ea9b1")
    version("2.3.0", sha256="9c07a2b7947cc169fc1713ad462ccc43a704076447893a1fd25bdda5eec4aab6")
    version("2.1.1", sha256="016ac5ece1808cd1100be72f90da4fa59ea41de487587a3283c6c981381cc216")
    version("2.1.0", sha256="1c9c35c039ad3a9795a278447db6da0a4ec1a1d223bf7d64687ad28f673b7ae8")
    version("2.0.1", sha256="1e43be17045a881c95cedc843d72fe9c1e53239b02ed179c1e39e041ebcd7dad")
    version("2.0.0", sha256="8b5b11197d1308dfc1fe20efd6a656e0c833dbec2807e2292967f6e2f7c0420f")
    version("1.1.9", sha256="1a666513157905aa0e53a13fac602b5673dcafb04a869100a85cd3f000c2ed0d")
    version("1.1.8", sha256="3cc426dcf38397637e889efd9567b06d55dd23fb4e65cc0381eb8103a411d104")
    version("1.1.7", sha256="b22d3274c9bbce695dd13a37083c6ce93741abc3d1d98712ad57b5c5c6adba26")
    version("1.1.6", sha256="da1eb2498e9eda60d8526d11cd3bcbf43c698657ee38bc1cfd969b2014f0d118")

    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            self.define("BOOST_UT_ENABLE_INSTALL", True),
            self.define("BOOST_UT_BUILD_TESTS", False),
            self.define("BOOST_UT_BUILD_EXAMPLES", False),
            self.define("BOOST_UT_BUILD_BENCHMARKS", False)
        ]
        return args
