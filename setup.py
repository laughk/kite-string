#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from kite.version import get_version

setup(

    name='kite-string',
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

)

