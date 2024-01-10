#!/usr/bin/env python

'''Flexible bracelet based on closed loop space filling curve.
'''

import solid2 as sd

if __name__ == '__main__':
    fn = 64

    size = 64
    h = 7
    final = sd.square(size, center=True)
    notch = sd.square([size,size/5], center=True)
    notch = sd.translate([size*3/5+1,0])(notch)
    final -= sd.union()(*[sd.rotate(i*90)(notch) for i in range(4)])
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


