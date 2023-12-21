#!/usr/bin/env python3

import matplotlib
# matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import solid2 as sd
# from solid.utils import *
import sys



def xy(vec):
    return vec.real, vec.imag

def snowflake(r=1, w=2, l=8):
    # w = (1 + 1j*np.sqrt(3))/2  # sixth root of unity
    dot = sd.circle(r, _fn=6)
    edge = sd.hull()(dot, sd.translate([l, 0])(dot))
    edge2 = sd.hull()(dot, sd.translate([l/2, 0])(dot))
    branch = edge
    branch += sd.translate([l,0])(edge)
    branch += sd.translate([2*l,0])(edge)
    # branch += sd.translate([3*l,0])(edge)
    branch += sd.translate([1.5*l,0])(sd.rotate(60)(edge))
    branch += sd.translate([1.5*l,0])(sd.rotate(-60)(edge))
    branch += sd.translate([2.25*l,0])(sd.rotate(60)(edge2))
    branch += sd.translate([2.25*l,0])(sd.rotate(-60)(edge2))
    # branch += sd.translate([3*l,0])(sd.rotate(60)(edge2))
    # branch += sd.translate([3*l,0])(sd.rotate(-60)(edge2))
    flake = sd.union()(*[sd.rotate(i*60)(branch) for i in range(6)])
    flake += sd.circle(3*r, _fn=6)
    return flake
    edge = sd.translate([0, -w/2])(edge)
    edge += sd.translate([l,0])(dot)
    flake = sd.union()(*[sd.rotate(i*60)(edge) for i in range(6)])
    flake += dot
    level = sd.translate([3*l,0])(flake)
    flake += sd.union()(*[sd.rotate(i*60)(level) for i in range(6)])
    flake += sd.union()(*[sd.rotate(i*60)(sd.translate([l,0])(edge)) for i in range(6)])
    return flake
    # For level 3
    flake+= sd.union()(*[sd.rotate(i*60)( sd.translate([9*l,0])(flake)) for i in range(6)])
    # level += sd.translate([2*l,0])(edge)

if __name__ == '__main__':
    flake = snowflake()
    flake = sd.linear_extrude(height=7.5)(flake)
    print(sd.scad_render(flake))
    exit(0)

limit = 5
# Equilateral triangle
theta = np.linspace(0, 2*np.pi, 4)[:-1]
theta = np.exp(1j*theta)
level = [np.exp(1j*theta)]
for i in range(limit-1):
    level.append(gosper_iter(level[i]))


fig, ax = plt.subplots()
# plt.axis('off')
resolution = 512

k = 5
limit = k+2
bound = (-limit, limit)
ax.set_aspect('equal')
ax.set_xlim(*bound)
ax.set_ylim(*bound)


iter = 3
# dragon, = ax.plot(*xy(np.array(list(gosper_path(*theta[:2], iter)))), 'b', linewidth=1)
# dragon, = ax.plot(*xy(theta[1]*np.array(list(gosper_path(*theta[:2], iter)))), 'r', linewidth=1)
# dragon, = ax.plot(*xy(theta[2]*np.array(list(gosper_path(*theta[:2], iter)))), 'g', linewidth=1)
# plt.show()

dragon = np.array(list(gosper_path(*theta[:2], iter)))
dragon = np.concatenate([dragon, theta[1]*dragon, theta[2]*dragon])

gosper = polygon(points=list(zip(*xy(12.5*dragon))))
gosper = minkowski()(gosper, circle(r=.15))

gosper = linear_extrude(height=10)(gosper)
print(scad_render(gosper))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
