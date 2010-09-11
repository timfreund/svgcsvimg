# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='svgcsvimg',
    version='1.0',
    description='Command line utility that generates a set of PNG images from an SVG template and data provided in a CSV file.',
    author='Tim Freund',
    author_email='tim@freunds.net',
    license = 'MIT License',
    url='http://github.com/timfreund/svgcsvimg',
    install_requires=[
        # requires rsvg, available on Ubuntu from python-gnome2-desktop
                ],
    packages=['svgcsvimg'],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    svgcsvimg = svgcsvimg:execute
    """,
)
