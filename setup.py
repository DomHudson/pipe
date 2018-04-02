#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'pipe',
    version = '0.0.1',
    description = 'Mulithread work but retain job ordering.',
    author = 'Dom Hudson',
    author_email = 'dom.hudson@thoughtriver.com',
    url = 'https://www.thoughtriver.com',
    packages = find_packages(),
    install_requires = [],
    dependency_links = []
)
