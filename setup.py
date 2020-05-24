from setuptools import setup
import os
import sys

PKG_NAME = "lexical"

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, PKG_NAME, 'version.py')) as f:
    exec(f.read(), version)

setup(
    name = PKG_NAME,
    version=version['__version__'],
    description=('A simple lexer written in Python and enumerations'),
    long_description=long_description,
    author='Jared Dyreson',
    author_email='jareddyreson@csu.fullerton.edu',
    url='https://github.com/JaredDyreson/lexical',
    license='GNU GPL-3.0',
    packages=[PKG_NAME],
    install_requires = [
      'aenum'
    ],
    include_package_data=True,
    classifiers=['Programming Language :: Python :: 3.8']
)

