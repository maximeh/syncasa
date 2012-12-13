#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

VERSION = '0.1'
setup(
    name='syncasa',
    version=VERSION,
    py_modules=['syncasa'],
    author='Maxime Hadjinlian',
    author_email='maxime.hadjinlian@gmail.com',

    maintainer='Maxime Hadjinlian',
    maintainer_email='maxime.hadjinlian@gmail.com',

    description='Sync a folder with your Picasa account',
    url='http://google.com',

    license='GPL',

    keywords='picasa google photo sync',
    install_requires=['gdata>=2.0.17', 'pyinotify>=0.9.3'],
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points={
      'console_scripts': ['syncasa = syncasa:main', ]}
)
