#!/usr/bin/env python

from distutils.core import setup

setup(name='nsga2',
      version='0.2',
      description='NSGA-II Algorithm implementation',
      author='Wojciech Reszelewski, Kamil Mielnik',
      author_email='wreszelewski@gmail.com',
      url = "https://github.com/wreszelewski/nsga2",
      packages=['nsga2', 'nsga2.problems'],
     )
