import solid2 as sd

if __name__ == '__main__':
    fn = 64

    size = 64
    size = size*2/3.141592
    h = 7
    final = sd.square(size, center=True)
    edge = sd.translate([size/2,0])(sd.circle(d=size))
    final += sd.union()(*[sd.rotate(i*90)(edge) for i in range(4)])
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)


