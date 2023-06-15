# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import Distribution, find_packages, setup


PACKAGE = 'graphonomy'


def _get_version():
    """"Helper to get the package version."""

    version_path = Path() / PACKAGE / 'version.py'
    if not version_path.exists():
        return None
    with open(version_path, 'r') as version_file:
        ns = {}
        exec(version_file.read(), ns)
    return ns['__version__']


# Packages to exclude
exclude_packages = [
    # '',
    'tests'
]

setup(
    name=PACKAGE,
    version=_get_version(),
    packages=find_packages(include=['graphonomy'],exclude=exclude_packages),
    # package_dir={'':'graphonomy'},
    author='',
    author_email='',
    maintainer='Nima Ghorbani',
    maintainer_email='nima.gbani@gmail.com',
    url='',
    description='',
    license='See LICENSE.txt',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    dependency_links=[],
    classifiers=[
        "Intended Audience :: Research",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10", ],
)
