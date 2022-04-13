#!/usr/bin/env python3

from distutils.core import setup

setup(name='glyph-finder',
      version='1',
      description='finds Linux fonts containing glyphs for sets of characters',
      author='Melissa Boiko',
      author_email='melissa@namakajiri.net',
      url='https://github.com/melissaboiko/glyph-finder',
      packages=['glyph_finder'],
      scripts=['bin/glyph-viewer'],
     )
