import solid2 as sd

if __name__ == '__main__':
    fn = 64

    size = 64
    h = 7
    final = sd.square(size, center=True)
    final = sd.linear_extrude(h)(final)
    final = sd.scad_render(final, file_header=f'$fn={fn};')
    print(final)

