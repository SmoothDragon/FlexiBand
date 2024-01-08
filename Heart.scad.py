#!/usr/bin/env python

'''
'''

import solid2 as sd

def heart(size):
    Heart = sd.square(size, center=True)
    curve = sd.circle(d=size)
    Heart += sd.translate([size/2,0])(curve)
    Heart += sd.translate([0,size/2])(curve)
    return Heart

def splitFour(shape, x, y, gap=.1, MAX=1000):
    splitter = sd.square([MAX, gap], center=True)
    shape -= sd.translate([x,0])(sd.rotate(90)(splitter))
    shape -= sd.translate([0,y])(splitter)
    return shape

if __name__ == '__main__':
    fn = 64

    size = 50
    gap = 1
    h = 10
    final = heart(size)
    final = sd.rotate(45)(final)
    final = splitFour(final, 0,11, gap=gap)
    final = splitFour(final, 15,-2, gap=gap)
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


