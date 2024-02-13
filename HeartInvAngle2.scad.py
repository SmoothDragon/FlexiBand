#!/usr/bin/env python

'''
'''

import solid2 as sd
import numpy as np
import svgSCAD as svg

def heart(size):
    theta = np.arctan(2/np.pi)*180/np.pi
    halve = sd.square([size, size*np.pi/2], center=True)
    halve += sd.translate([0,size*np.pi/4])(sd.circle(d=size))
    halve = sd.rotate(-theta)(halve)
    halve &= svg.halfPlane('E')
    full = halve + sd.mirror([1,0])(halve)
    full = sd.translate([0,-size/4])(full)
    return full


if __name__ == '__main__':
    fn = 64

    layer = .2
    size = 50
    gap = 1
    h = 5
    layers = int(h/layer)
    final = sd.union()(*[sd.linear_extrude((l+1)*layer)(heart(size-l*layer/10)) for l in range(layers)])
    final += sd.mirror([0,0,1])(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


