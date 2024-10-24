# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip._internal.req import parse_requirements
import re, ast

# get version from __version__ variable in automation_example/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('automation_example/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Parse the requirements.txt file
requirements = parse_requirements("requirements.txt", session=False)

# Extract the required packages from the parsed requirements
install_requires = [str(requirement.requirement) for requirement in requirements]

setup(
    name='automation_example',
    version=version,
    description='An example of an automated Workflow between different documents',
    author='Felix Isensee',
    author_email='f.isensee@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
