#!/usr/bin/env python

# BittrexAPI: Python Bittrex API implementation
#
# Copyright (c) 2014 - Albert Puigsech Galicia (albert@puigsech.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import BittrexAPI

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='BittrexAPI',
    version=BittrexAPI.__version__,
    description=BittrexAPI.__description__,
    license=BittrexAPI.__license__,
    author=BittrexAPI.__author__,
    author_email=BittrexAPI.__author_email__,
    url=BittrexAPI.__url__,
    packages=['BittrexAPI'],
    include_package_data=True,
)