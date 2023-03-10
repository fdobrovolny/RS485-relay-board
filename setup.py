"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_namespace_packages


# The version of this tool is based on the following steps:
# https://packaging.python.org/guides/single-sourcing-package-version/
VERSION = {}

with open("./src/rs485_relay_board/__init__.py") as fp:
    # pylint: disable=W0122
    exec(fp.read(), VERSION)

setup(
    name="rs485-relay-board",
    author="Filip Dobrovolny",
    author_email="dobrovolny.filip@gmail.com",
    url="https://github.com/fdobrovolny/RS485-relay-board",
    description="Python library for interaction with R4D8A08, R4D3B16 and similar.",
    version=VERSION.get("__version__", "0.0.0"),
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=["tests"]),
    install_requires=[
        "setuptools>=45.0",
        "minimalmodbus>=2.0.1",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
        "Topic :: System :: Hardware",
    ],
)
