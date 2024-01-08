#!/usr/bin/env python

import solid2 as sd
import numpy as np

def hardH(r, epsilon=0.001):
    '''Make an H shape that is essentially 1D.
    '''
    final = sd.square([2*r,epsilon], center=True)
    a = 2**.5*r
    final += sd.translate([r,0])(sd.square([epsilon, a], center=True))
    final += sd.translate([-r,0])(sd.square([epsilon, a], center=True))
    return final

def iterHardH(R, n=2):
    base = hardH(R)
    Ry = 2**-.5*R
    level = base
    for i in range(n):
        level = base + sd.union()(*[sd.translate(ij)(sd.scale([.5, .5, 1])(level)) for ij in [(R,Ry), (-R,Ry), (R,-Ry), (-R,-Ry)]])
    # R = 4*(1+ratio)*r
    # level = base + sd.union()(*[sd.translate(ij)(level) for ij in [(R,R), (-R,R), (R,-R), (-R,-R)]])
    # R = 8*(1+ratio)*r
    # level = base + sd.union()(*[sd.translate(ij)(level) for ij in [(R,R), (-R,R), (R,-R), (-R,-R)]])
    return level

if __name__ == '__main__':
    fn = 64

    r = 25
    w = .4
    size = 10
    frame = iterHardH(r, n=3)
    final = sd.minkowski()(frame, sd.square(3*w, center=True))
    final -= sd.minkowski()(frame, sd.square(1*w, center=True))
    final = sd.linear_extrude(size)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


