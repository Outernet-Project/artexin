"""
fetch_and_zip.py: Fetch specified pages and zip them up

This demo script uses the higher-level functions from ``artexin.pack`` module
to fetch and zip up specified pages one by one. Also seee
``fetch_and_zip_batch.py`` example for batch operation using an even
higher-level API.

Copyright 2014, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""
import time

from artexin.pack import collect
from artexin.preprocessor_mappings import get_preps


__author__ = 'Outernet Inc <branko@outernet.is>'
__version__ = 0.1


PAGES = [
    'http://www.nasa.gov/press/2014/may/nasa-releases-earth-day-global-selfie-mosaic-of-our-home-planet',
    'http://en.wikipedia.org/wiki/Sunflower',
    'http://en.wikipedia.org/wiki/Logarithm',
    'http://freepythontips.wordpress.com/2013/07/30/20-python-libraries-you-cant-live-without/',
]


if __name__ == '__main__':
    start = time.time()
    for page in PAGES:
        print('Processing: %s' % page)
        collect(page, get_preps(page), base_dir='/vagrant')
    took = time.time() - start
    avg = took / len(PAGES)
    print('Took %s seconds (avg: %s seconds)' % (took, avg))
