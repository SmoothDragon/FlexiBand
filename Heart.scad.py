#!/usr/bin/env python

'''
'''
import numpy as np
import solid2 as sd

def heart(size):
    Heart = sd.square(size)
    curve = sd.circle(d=size)
    Heart += sd.translate([size/2,size])(curve)
    Heart += sd.translate([size,size/2])(curve)
    return Heart

def splitFour(shape, x, y, gap=.1, MAX=1000):
    splitter = sd.square([MAX, gap], center=True)
    shape -= sd.translate([x,0])(sd.rotate(90)(splitter))
    shape -= sd.translate([0,y])(splitter)
    return shape

if __name__ == '__main__':
    fn = 256

    size = 40
    gap = .4
    inset = 2
    alpha = .5
    beta = .25
    h = 10
    final = heart(size)
    final = sd.rotate(45)(final)
    small = sd.scale(beta)(final)
    small = sd.translate([0,inset])(small)
    small += sd.translate([0,inset])(sd.square([gap,2*inset], center=True))
    top = sd.translate([0,1.01*size*2**.5])(sd.rotate(180)(small))
    left = sd.translate([-size*(.5**.5),size*(2**.5)])(sd.rotate(-135)(small))
    right = sd.translate([size*(.5**.5),size*(2**.5)])(sd.rotate(135)(small))
    lower_left = sd.translate([-alpha*size,alpha*size])(sd.rotate(-45)(small))
    lower_right = sd.translate([alpha*size,alpha*size])(sd.rotate(45)(small))
    final -= small
    final -= top
    final -= left
    final -= right
    final -= lower_left
    final -= lower_right
    # final = splitFour(final, 0,11, gap=gap)
    # final = splitFour(final, 15,-2, gap=gap)
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


