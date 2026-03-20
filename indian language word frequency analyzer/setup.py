# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="indian-language-word-frequency-analyzer",
    version="1.0.0",
    author="Jaj Adhav",
    description="Word frequency analyzer for Indian languages",
    long_description=long_description,
    url="https://github.com/jayjadhav-max/indian-language-word-frequency-analyzer",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["nltk>=3.6", "numpy>=1.19"],
)