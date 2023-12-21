#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import math
import numpy as np

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
# from solid import *
# from solid.utils import *

import solid2 as sd


def kochSnowflake(diameter=20, iterations=3):
    rad = diameter/2
    xrad = rad*math.sqrt(3)/2
    yrad = rad/2
    # Make an equilateral triangle with circumradius=rad
    koch = [sd.polygon([(0,rad), (-xrad, -yrad), (xrad, -yrad)])]
    # Rotate triangle and union to make hexagram
    hexagram = sd.union()(koch[0], sd.rotate(60)(koch[0]))
    koch.append(hexagram)
    if iterations < 2:
        return koch[iterations]
    for level in range(1, iterations):  # indicates level we are building from
        shape = koch[level]
        for i in range(6):
            shape = sd.union()(
                sd.rotate(60)(shape),
                sd.translate([0,rad*2/3,0])(sd.scale([1/3,1/3,1])(koch[level])),
                )
        koch.append(shape)
    return koch[-1]

def kochBarrel(diameter=50, iterations=3, levels=100):
    snowflake = kochSnowflake(diameter=diameter, iterations=iterations)
    X = np.linspace(0, 1, num=levels+1)
    Y = np.sqrt(1-X*X)
    layers = []
    for i in range(len(X) - 1):
        if X[i] > .8:
            break
        piece = linear_extrude(
                    height=diameter/levels/2,
                    scale=Y[i+1]/Y[i],
                    slices=1,
                    )(scale(Y[i])(snowflake))
        piece = translate([0,0,i*diameter/levels/2])(piece)
        layers.append(piece)
    upper = union()(*layers)
    return union()(upper,
                   rotate([0,180,0])(upper),
                   )


def twistTree(level_h = 30, diameter=50, num_iter=4):
    flake=kochSnowflake(diameter=diameter, iterations=num_iter)
    flake2=kochSnowflake(diameter=diameter*3**-.5, iterations=num_iter)
    flake2 = sd.rotate(30)(flake2)
    delta = 1-3**-.5
    piece = sd.linear_extrude(height=diameter/3, scale=1/3, twist=60)(flake)
    block = piece
    piece = sd.linear_extrude(height=diameter/3, scale=1, twist=30)(flake2)
    # piece = sd.translate([0,0,-1])(piece)
    # piece = sd.linear_extrude(height=3**.5*delta*diameter, scale=1/(1-delta)-1, center=False)(flake2)
    block += piece
    # Repeat
    piece = sd.scale(1/3**.5)(block)
    # piece = sd.rotate([0,0,15])(piece)
    piece = sd.translate([0,0,diameter*(1/3)])(piece)
    block += piece
    # Repeat
    piece = sd.scale(1/3)(block)
    # piece = sd.rotate([0,0,30])(piece)
    piece = sd.translate([0,0,diameter*(1/3+1/3**1.5)])(piece)
    block += piece
    # Repeat
    piece = sd.scale(1/9)(block)
    # piece = sd.rotate([0,0,30])(piece)
    piece = sd.translate([0,0,diameter*(1/3+1/3**1.5+1/3**2+1/3**2.5)])(piece)
    block += piece
    block = sd.scale([1,1,1.5])(block)
    block = sd.scale(2)(block)
    return block

def twistTree2(level_h = 30, diameter=50, num_iter=3):
    flake=kochSnowflake(diameter=diameter, iterations=num_iter)
    flake2=kochSnowflake(diameter=diameter*3**-.5, iterations=num_iter)
    flake2 = sd.rotate(30)(flake2)
    delta = 1-3**-.5
    piece = sd.linear_extrude(height=diameter/3, scale=1/3, twist=60)(flake)
    block = piece
    piece = sd.linear_extrude(height=diameter/3, scale=1, twist=-30)(flake2)
    # piece = sd.translate([0,0,-1])(piece)
    # piece = sd.linear_extrude(height=3**.5*delta*diameter, scale=1/(1-delta)-1, center=False)(flake2)
    block += piece
    # Repeat
    piece = sd.scale(1/3**.5)(block)
    # piece = sd.rotate([0,0,15])(piece)
    piece = sd.translate([0,0,diameter*(1/3)])(piece)
    block += piece
    # Repeat
    piece = sd.scale(1/3)(block)
    # piece = sd.rotate([0,0,30])(piece)
    piece = sd.translate([0,0,diameter*(1/3+1/3**1.5)])(piece)
    block += piece
    # Repeat
    piece = sd.scale(1/9)(block)
    # piece = sd.rotate([0,0,30])(piece)
    piece = sd.translate([0,0,diameter*(1/3+1/3**1.5+1/3**2+1/3**2.5)])(piece)
    block += piece
    block = sd.scale([1,1,1.5])(block)
    block = sd.scale(2)(block)
    return block


def straightTree(level_h = 30, diameter=50, num_iter=3):
    flake=kochSnowflake(diameter=diameter, iterations=num_iter)
    flake2=kochSnowflake(diameter=diameter*3**-.5, iterations=num_iter)
    flake2 = sd.rotate(30)(flake2)
    delta = 1-3**-.5
    piece = sd.linear_extrude(height=diameter/3, scale=1/3, center=False)(flake)
    block = piece
    piece = sd.linear_extrude(height=diameter/3, scale=1, center=False)(flake2)
    # piece = sd.linear_extrude(height=3**.5*delta*diameter, scale=1/(1-delta)-1, center=False)(flake2)
    block += piece

    # second layer
    piece = sd.linear_extrude(height=diameter/3**1.5, scale=1/3, center=False)(flake2)
    piece = sd.translate([0,0,diameter/3])(piece)
    block += piece
    flake = sd.scale(1/3)(flake)
    piece = sd.linear_extrude(height=diameter/3**1.5, scale=1, center=False)(flake)
    piece = sd.translate([0,0,diameter/3])(piece)
    block += piece

    # Repeat
    piece = sd.scale(1/3)(block)
    piece = sd.translate([0,0,diameter*(1/3+1/3**1.5)])(piece)
    block += piece
    
    # Repeat
    piece = sd.scale(1/9)(block)
    piece = sd.translate([0,0,diameter*(1/3+1/3**1.5+1/3**2+1/3**2.5)])(piece)
    block += piece

    block = sd.scale([1,1,1.5])(block)
    # block = sd.translate([0,diameter,0])(piece)
    # block = sd.union()(*[sd.rotate([0,0,i*60])(block) for i in range(6)])
    # block += sd.cylinder(d=np.sqrt(3)*diameter, h=level_h)
    # block -= piece
    # piece = piece - sd.linear_extrude(height=2*level_h, center=False)(sd.rotate([0,0,30])(sd.scale(1/np.sqrt(3))(kochSnowflake(iterations=4))))
    # piece = piece - sd.linear_extrude(height=4*level_h, center=True)(sd.scale(1/3)(flake))
    return block

if __name__ == '__main__':
    # block = straightTree()
    d = 30
    epsilon=.0001
    final = kochSnowflake(diameter=d, iterations=3)
    limb = sd.translate([0,d+epsilon,0])(final)
    limb += sd.translate([0,d/2,0])(sd.square([1,2], center=True))
    final += sd.union()(*[sd.rotate(i*60)(limb) for i in range(6)])
    final = sd.linear_extrude(10)(final)
    # final = twistTree2()

    fn=256
    print(sd.scad_render(final, file_header=f'$fn={fn};'))

    # print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())
    # scad_render_to_file(a, file_out, include_orig_code=True)


