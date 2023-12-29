#!/usr/bin/env python3

import solid2 as sd
import numpy as np


def smoothHex(leg, r, w=2):
    '''Make a square shaped X out fo circluar arcs with radius r.
    Square side length with be 6*r.
    '''
    scale = 3
    center = sd.circle(r=r, _fn=6)
    branch = sd.square([leg, w],center=True)
    branch = sd.translate([.5*leg, 0])(branch)
    branch += sd.translate([leg, 0])(center)
    arm = sd.translate([0,-w/2])(sd.square([2*leg, w]))
    branch += arm
    figure = sd.union()(*[sd.rotate(i*60)(branch) for i in range(6)])
    figure += sd.translate([2*scale*leg,0])(figure)
    figure = sd.union()(*[sd.rotate(i*60)(figure) for i in range(6)])
    arm2 = sd.translate([0,-w/2])(sd.square([4*leg, w]))
    figure += sd.union()(*[sd.rotate(i*60)(arm2) for i in range(6)]) 
    figure += sd.translate([2*scale**2*leg,0])(figure)
    figure = sd.union()(*[sd.rotate(i*60)(figure) for i in range(6)])
    arm3 = sd.translate([0,-w/2])(sd.square([16*leg, w]))
    figure += sd.union()(*[sd.rotate(i*60)(arm3) for i in range(6)]) 
    figure += sd.translate([2*scale**3*leg,0])(figure)
    figure = sd.union()(*[sd.rotate(i*60)(figure) for i in range(6)])
    arm4 = sd.translate([0,-w/2])(sd.square([32*leg, w]))
    figure += sd.union()(*[sd.rotate(i*60)(arm4) for i in range(6)]) 
    return figure

if __name__ == '__main__':
    fn = 64

    r = .5
    leg = 1 # n = 3  # iterations
    final = smoothHex(leg, r)
    # final = sd.linear_extrude(size)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)
