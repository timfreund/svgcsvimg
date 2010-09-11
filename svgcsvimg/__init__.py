#!/usr/bin/env python
# Copyright (C) 2010 Tim Freund and contributors.
# See LICENSE for details. (MIT)

"""
Command line utility that generates a set of PNG images from an SVG
template and data provided in a CSV file.

Variable names are determined from the first row of the CSV file, and
the file *must* contain a 'filename' column.  The resulting PNG images
are created using the CSV supplied filename.

Does your text render as a solid rectangle?  There is a bug in the way
the rsvg library handles flowable elements that triggers this behavior.
Converting flowable text to single line is a (painful) workaround.
"""

import cairo
import csv
import os
import rsvg
import sys
from optparse import OptionParser

def create_arg_parser():
    parser = OptionParser(usage="usage: %%prog\n%s" % __doc__)
    parser.add_option("-t", "--template", dest="template",
                      help="SVG template")
    parser.add_option("-o", "--output-directory", dest="output_dir",
                      help="Output Directory")
    parser.add_option("-c", "--csv",
                      dest="csv", 
                      help="CSV data")
    return parser

def render_svg(svg_data, output_path):
    svg = rsvg.Handle(data=svg_data)
    width, height = svg.get_dimension_data()[0:2]
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    svg.render_cairo(ctx)

    if os.path.exists(output_path):
        print "Refusing to overwrite %s" % output_path
    else:
        output_file = open(output_path, "w")
        surface.write_to_png(output_file)
        output_file.close()
    
def execute():
    arg_parser = create_arg_parser()
    (options, args) = arg_parser.parse_args()

    if None in [options.template, options.csv]:
        arg_parser.print_help()
        sys.exit(-1)

    template_file = open(options.template, "r")
    template = template_file.read()
    template_file.close()

    csv_file = open(options.csv, "r")
    csv_reader = csv.reader(csv_file)
    keys = csv_reader.next()

    for row in csv_reader:
        variables = {}
        for idx, key in enumerate(keys):
            variables[key] = row[idx]

        svg_data = template
        for k, v in variables.items():
            svg_data = svg_data.replace(k, v)

        if options.output_dir is None:
            variables['output_path'] = "%s.png" % variables['filename']
        else:
            variables['output_path'] = "%s.png" % os.path.sep.join([options.output_dir,
                                                                    variables['filename']])

        render_svg(svg_data, variables['output_path'])

if __name__ == "__main__":
    execute()

