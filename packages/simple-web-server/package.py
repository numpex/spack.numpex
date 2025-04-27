# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class SimpleWebServer(CMakePackage):
    """A very simple, fast, multithreaded, platform independent HTTP and HTTPS server and client library implemented using C++11 and Asio (both Boost.Asio and standalone Asio can be used). 
    Created to be an easy way to make REST resources available from C++ applications."""

    homepage = "https://gitlab.com/eidheim/Simple-Web-Server"
    url = "https://gitlab.com/eidheim/Simple-Web-Server/-/archive/v3.1.1/Simple-Web-Server-v3.1.1.tar.gz"
    git = "https://gitlab.com/eidheim/Simple-Web-Server.git"

    maintainers("prudhomm")
    license("MIT", checked_by="prudhomm")

    version("master", branch="master")
    version("3.1.1", sha256="f8f656d941647199e0a2db3cb07788b0e8c30d0f019d28e6ee9281bc48db132d")
    version("3.1", sha256="a727b901cccfa2eb6d7dc8abb860c98d1abeefa4b6b23e419a7476275a08aa91")
    version("3.0.2", sha256="9997079979c542e49809c4ce20942f2eed60b34505b9e757d08966488d18d319")

    variant("ssl", default=True, description="Enable SSL support")
    
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("boost +system+thread+filesystem+regex")
    depends_on("openssl", when="+ssl")

    patch("fix-cmakelists.patch", when="@3.0:")

    def cmake_args(self):
        args = [self.define_from_variant("USE_OPENSSL", "ssl")]
        return args
