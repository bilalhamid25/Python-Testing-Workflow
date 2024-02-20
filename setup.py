"""
# setup.py
"""

from typing import List
from setuptools import setup, find_packages

# pylint: disable=unspecified-encoding
with open("README.md", encoding="utf-8", mode="r") as readme_file:
    long_description = readme_file.read()


def read_requirements(file_path: str) -> List[str]:
    """
    Read the requirements from a file.

    Args:
        file_path: The path to the requirements file.

    Returns:
        A list of the requirements.
    """
    with open(file_path, "r") as requirements_file:
        return requirements_file.read().splitlines()


setup(
    name="calculator",
    version="0.1",
    author="Sharjeel M.",
    author_email="sharjeelmazhar@gmail.com",
    description="A simple Python package for basic arithmetic operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sharjeelmazhar/test",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="calculator arithmetic package",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements_dev.txt"),
    },
    project_urls={
        "Source": "https://github.com/sharjeelmazhar/test",
        "Bug Reports": "https://github.com/sharjeelmazhar/test/issues",
    },
)
