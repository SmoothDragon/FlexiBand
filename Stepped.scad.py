#!/usr/bin/env python

'''Flexible bracelet based on closed loop space filling curve.
'''

import solid2 as sd

if __name__ == '__main__':
    fn = 64

    size = 64
    h = 7
    final = sd.square([size, size*3/5], center=True)
    final += sd.square([size*7/5,size/5], center=True)
    final += sd.rotate(90)(final)
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


