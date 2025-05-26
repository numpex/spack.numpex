# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyRay(PythonPackage):
    """Ray provides a simple, universal API for building distributed applications."""

    homepage = "https://github.com/ray-project/ray"
    url = "https://files.pythonhosted.org/packages/cp312/r/ray/ray-2.46.0-cp312-cp312-manylinux2014_x86_64.whl"

    license("Apache-2.0")

    version("2.46.0", sha256="5cec1edda93f618ffd2301f81d5398037f03fa9b16825e7e4d8a00ae7a9a4381")

    # FIXME: Allow for other python versions
    depends_on("python@3.12", type=("build", "run"))

    with default_args(type=("run")):
        depends_on("py-click")
        depends_on("py-filelock")
        depends_on("py-jsonschema")
        depends_on("py-msgpack")
        depends_on("py-packaging")
        depends_on("py-protobuf")
        # Higher versions have ABI compatibility because we don't build ray from source
        depends_on("protobuf@:3.20")
        depends_on("py-pyyaml")
        depends_on("py-requests")
        depends_on("py-watchfiles")

        # Default deps
        depends_on("py-aiohttp")
        depends_on("py-aiohttp-cors")
        depends_on("py-colorful")
        depends_on("py-opencensus")
        depends_on("py-prometheus-client")
        depends_on("py-pydantic")
        depends_on("py-py-spy")
        depends_on("py-smart-open")
        depends_on("py-virtualenv")
