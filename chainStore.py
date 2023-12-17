#!/usr/bin/env python3

from solid import *
from solid.utils import *
import solid as sp  # SolidPython

from math import atan, sqrt
import math


def parseArguments():
    # Argument parsing
    import argparse
    parser = argparse.ArgumentParser(
        description='Generate SCAD for half Sierpinski cube.')
    parser.add_argument('-n', action='store', default='20', dest='iterations',
        type=int, help='Number or iterations to apply.')
    parser.add_argument('--size', action='store', default='81', dest='size',
        type=float, help='Side length (in millimeters) of cube.')
    parser.add_argument('--twist', action='store', default=22.5, dest='twist',
        type=float,)
    parser.add_argument('--shift', action='store', default=10, dest='shift',
        type=float,)
    parser.add_argument('--scale', action='store', default=.9, dest='scale_xyz',
        type=float,)
    return parser.parse_args()


def octogon(inradius=4):
    # TODO: make points from parameters
    x = inradius
    y = inradius/(math.sqrt(2)+1)  # To make regular octogon
    points = [(x,y), (y,x), (-y,x), (-x,y), (-x,-y), (-y,-x), (y,-x), (x,-y)]
    shape = sp.polygon(points=points)
    return shape

def octo_path(length):
    shape = octogon()
    rod = sp.linear_extrude(height=length, center=True, convexity=10, twist=0)(shape)
    cut_shape = sp.polygon([(length/2-4, 0), (-4, length/2), (-4, -length/2)])
    cut_block = sp.linear_extrude(height=8, center=True, convexity=10)(cut_shape)
    cut_block = rotate([90, 0, 0])(cut_block)
    return intersection()(cut_block, rod)


def make_link():
    major = octo_path(47)
    minor = rotate([0,-90,0])(octo_path(31))
    left = translate([-31/2+4,0,0])(major)
    right = translate([31/2-4,0,0])(rotate([0,0,180])(major))
    bottom = translate([0,0,-47/2+4])(minor)
    top = translate([0,0,47/2-4])(rotate([180,0,0])(minor))
    link = top+right+bottom+left
    link = rotate([90,0,0])(link)
    return link

def make_chain():
    link = rotate([45,0,0])(make_link())
    twist_link = rotate([90,0,0])(link)
    chain = link
    chain += translate([12,12,0])(twist_link)
    chain += translate([-12,-12,0])(twist_link)
    chain += translate([24,24,0])(link)
    chain += translate([-24,-24,0])(link)
    return chain


if __name__ == '__main__':
    args = parseArguments()

    final = make_chain()
    print(scad_render(final))
