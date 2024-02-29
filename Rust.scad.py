#!/usr/bin/env python

'''Invertible RUST
'''

import solid2 as sd
import svgSCAD as d2


def ann(plane=None):
    annulus = sd.circle(3)-sd.circle(1)
    if plane is not None:
        annulus = sd.intersection()(annulus, d2.halfPlane(plane))
    return annulus

if __name__ == '__main__':
    fn = 64

    size = 64
    h = 10
    vert = sd.square([2,10])
    # R
    final = vert
    final += sd.translate([2,4])(sd.square([1,6]))
    final += sd.translate([3,7])(sd.circle(3))
    final += sd.translate([3,3])(ann('N'))
    final += sd.translate([7,3])(ann('S'))
    # U
    pos = 8
    final += sd.translate([pos,3])(sd.square([2,7]))
    final += sd.translate([pos+3,3])(ann('S'))
    final += sd.translate([pos+4,3])(sd.square([2,7]))
    final += sd.translate([pos+7,3])(sd.intersection()(ann('S'), ann('W')))
    final += sd.translate([pos+7,0])(sd.square([3,2]))
    # S
    pos += 7
    final += sd.translate([pos,0])(sd.square([3,2]))
    final += sd.translate([pos+3,3])(ann('E'))
    final += sd.translate([pos+3,7])(ann('W'))
    final += sd.translate([pos+3,8])(sd.square([8,2]))
    # T
    pos += 5
    final += sd.translate([pos,8])(sd.square([6,2]))
    final += sd.translate([pos+2, 0])(vert)

    final = sd.scale(5)(final)

    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


