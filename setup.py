#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="lengths_converter",
    version=0.3,
    author="Rahul Shelke",
    author_email="srahul07@gmail.com",
    url="https://bitbucket.org/srahul07/length_converter/src/basic/",
    description="Easily convert lengths in Python",
    packages=["lengths"],
    keywords = "lengths",
    long_description=open("README").read(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)