#!/usr/bin/env python

from distutils.core import setup
from os.path import dirname, abspath, join


name = 'fbmessageparser'
version = '0.1.0'
package = join(
    dirname(abspath(__file__)), name
)


with open(join(package, '__init__.py'), 'w') as f:
    f.write("__version__ = '{}'".format(version))
    f.write('')


setup(
    name=name,
    version=version,
    description='Simple Facebook archive messages parser',
    author='Peter Badida',
    author_email='keyweeusr@gmail.com',
    url='https://github.com/KeyWeeUsr/' + name,
    download_url=(
        'https://github.com/KeyWeeUsr/' + name + '/tarball/'
        '{}'.format(version)
    ),
    packages=[name],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords=[name, 'facebook', 'message', 'parser'],
    license="License :: OSI Approved :: MIT License"
)
