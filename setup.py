#!/usr/bin/env python
# encoding: utf-8
"""
setup.py -- setup file for the pyana module

Created by Tim van Werkhoven (t.i.m.vanwerkhoven@xs4all.nl) on 2009-02-11.
Copyright (c) 2009 Tim van Werkhoven. All rights reserved.
"""
import sys

try:
	import numpy
	from numpy.distutils.core import setup, Extension
except:
	print "Could not load NumPy (numpy.distutils.core), required by this package. Aborting"
	sys.exit(1)

module_pyana = Extension('_pyana',
                    define_macros = [('MAJOR_VERSION', '0'),
                                     ('MINOR_VERSION', '3')],
                    include_dirs = [numpy.get_include()],
#                   libraries = [''],
#                   library_dirs = [''],
										extra_compile_args=["-O4", "-ffast-math"],
										extra_link_args=None,
                    sources = ['src/_pyana.c',
								'src/anarw.c',
#								'src/anarw.h',
#								'src/crunchstuff.h',
								'src/anacompress.c',
								'src/anadecompress.c'])

setup (name = 'pyana',
	version = '0.3.2',
	description = 'Python library to read ANA f0 files',
	author = 'Tim van Werkhoven',
	author_email = 'tim@astro.su.se',
	url = 'http://www.solarphysics.kva.se/~tim/',
	license = "GPL",
# This is for the python wrapper module:
    package_dir = {'pyana' : 'pyana'},
    packages = ['pyana'],
    ext_package = 'pyana',
# This is for the C module
	ext_modules = [module_pyana])
