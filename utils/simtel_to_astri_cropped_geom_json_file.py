#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# This script is provided under the terms and conditions of the MIT license:
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
... TODO
"""

__all__ = ['simtel_to_geom_json_file']

import argparse
import numpy as np

from datapipe.io import geometry_converter

import ctapipe

# Old version
from ctapipe.io import camera

# New version
#from ctapipe.instrument import camera


def simtel_to_geom_json_file(output_json_file=None):

    num_pixels_x = 40
    num_pixels_y = 40
    range_x = (-0.142555996776, 0.142555996776)
    range_y = (-0.142555996776, 0.142555996776)

    geom = camera.make_rectangular_camera_geometry(num_pixels_x,
                                                   num_pixels_y,
                                                   range_x,
                                                   range_y)

    # Convert and write the geom object

    if output_json_file is None:
        output_json_file = "astri_cropped.geom.json"

    geometry_converter.geom_to_json_file(geom, output_json_file)


def main():

    # PARSE OPTIONS ###########################################################

    desc = "Generate geom.json file form simtel a file."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("--output", "-o",
                        metavar="FILE",
                        help="The geom.json output file path")

    args = parser.parse_args()

    output_file = args.output

    simtel_to_geom_json_file(output_file)


if __name__ == "__main__":
    main()

