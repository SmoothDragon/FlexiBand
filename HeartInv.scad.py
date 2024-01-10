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
    halve += sd.mirror([1,0])(halve)
    return halve


if __name__ == '__main__':
    fn = 64

    size = 50
    gap = 1
    h = 10
    final = heart(size)
    # final = sd.rotate(45)(final)
    # final = splitFour(final, 0,11, gap=gap)
    # final = splitFour(final, 15,-2, gap=gap)
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


