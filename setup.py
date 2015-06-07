#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from kite.version import get_version

setup(

    name='kite-string',
    description='command-line HTTP request wrapper for takosan .',
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        kite=kite.cli:main
    ''',
    url='https://github.com/laughk/kite-string',
    author = 'Kei Iwasaki',
    author_email = 'me@laughk.org',
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

)

