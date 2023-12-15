#!/usr/bin/env python

'''Flexible bracelet based on closed loop space filling curve.
'''

from FlexiBand import *

if __name__ == '__main__':
    fn = 64

    r = 1
    ratio = .1
    n = 2  # iterations
    final = iterSmoothX(r, ratio, n)
    final = sd.scale(3)(final)
    size = 2**n * 4 * (1+ratio) * r  # side length or iteration
    size = 10 
    # final += sd.square(size, center=True)
    final = sd.linear_extrude(size)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


