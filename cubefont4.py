import svgwrite


def move(xy):
    return ("M", 120 * xy[0], 120 * (8-xy[1]))


def line(xy):
    return ("L", 120 * xy[0], 120 * (8-xy[1]))

def c(d):
    p = svgwrite.path.Path(None, fill='black', stroke='black', fill_rule='evenodd')
    p.push(move(transform_f(0, 0)))
    p.push(line(transform_f(0, 4)))
    p.push(line(transform_u(0, 4)))
    p.push(line(transform_u(4, 4)))
    p.push(line(transform_r(4, 0)))
    p.push(line(transform_r(0, 0)))
    p.push("Z")

    w = 0.04
    for t in [transform_f, transform_r, transform_u]:
        for x in range(4):
            x1 = w
            x2 = w
            if x == 0 and (t == transform_f or t == transform_u):
               x1 = 4 * w
            if x == 3 and (t == transform_r):
               x2 = 4 * w
            for y in range(4):
                y1 = w
                y2 = w
                if y == 0 and (t == transform_f or t == transform_r):
                     y1 = 4 * w
                if y == 3 and (t == transform_u):
                     y2 = 4 * w
                p.push(move(t(x + x1, y + y1)))
                p.push(line(t(x + x1, y + 1 - y2)))
                p.push(line(t(x + 1 - x2, y + 1 - y2)))
                p.push(line(t(x + 1 - x2, y + y1)))
                p.push("Z")
                
    d.add(p)

def transform_f(x, y):
    return (x, 2 - x / 2 + y)

def transform_u(x, y):
    return (x + y, 6 - x / 2 + y / 2)

def transform_r(x, y):
    return (4 + x, x / 2 + y)

def t_f(xy):
    return transform_f(xy[0], xy[1])

def t_u(xy):
    return transform_u(xy[0], xy[1])

def t_r(xy):
    return transform_r(xy[0], xy[1])

arrow_up_shape = [
    (0.4, 0),
    (0.4, 2.8),
    (0.1, 2.8),
    (0.5, 4),
    (0.9, 2.8),
    (0.6, 2.8),
    (0.6, 0)
]

arrow_down_shape = [(xy[0], 4-xy[1]) for xy in arrow_up_shape]
arrow_right_shape = [(xy[1], xy[0]) for xy in arrow_up_shape]
arrow_left_shape = [(4 - xy[0], xy[1]) for xy in arrow_right_shape]

def add_shape(d, shape, t):
    p = svgwrite.path.Path(None, fill='black', stroke='none')
    p.push(move(t(shape[0])))
    for x in range(1, len(shape)):
        p.push(line(t(shape[x])))
    p.push("Z")
    d.add(p)

def translate(x, y, t):
    def xf(xy):
        xy2 = (xy[0] + x, xy[1] + y)
        return t(xy2)
    return xf

def cube(filename, *shapes):
    dwg = svgwrite.Drawing("cube4\\"+filename, profile='tiny')
    c(dwg)
    for s in shapes:
        add_shape(dwg, s[0], s[1])
    dwg.save()

cube("R.svg",
     (arrow_up_shape, translate(3, 0, t_f)))
cube("L.svg",
     (arrow_down_shape, t_f))
cube("U.svg",
     (arrow_left_shape, translate(0, 3, t_f)))
cube("F.svg",
    (arrow_down_shape, t_r))
cube("B.svg",
    (arrow_up_shape, translate(3, 0, t_r)))
cube("D.svg",
    (arrow_right_shape, t_f))

cube("R2.svg",
     (arrow_up_shape, translate(3, 0, t_f)),
     (arrow_up_shape, translate(3, 0, t_u)))
cube("L2.svg",
     (arrow_down_shape, t_f),
     (arrow_down_shape, t_u))
cube("U2.svg",
     (arrow_left_shape, translate(0, 3, t_f)),
     (arrow_left_shape, translate(0, 3, t_r)))
cube("F2.svg",
     (arrow_down_shape, t_r),
     (arrow_right_shape, t_u))
cube("B2.svg",
     (arrow_up_shape, translate(3, 0, t_r)),
     (arrow_left_shape, translate(0, 3, t_u)))
cube("D2.svg",
     (arrow_right_shape, t_f),
     (arrow_right_shape, t_r))

cube("R2'.svg",
     (arrow_down_shape, translate(3, 0, t_f)),
     (arrow_down_shape, translate(3, 0, t_u)))
cube("L2'.svg",
     (arrow_up_shape, t_f),
     (arrow_up_shape, t_u))
cube("U2'.svg",
     (arrow_right_shape, translate(0, 3, t_f)),
     (arrow_right_shape, translate(0, 3, t_r)))
cube("F2'.svg",
     (arrow_up_shape, t_r),
     (arrow_left_shape, t_u))
cube("B2'.svg",
     (arrow_down_shape, translate(3, 0, t_r)),
     (arrow_down_shape, translate(3, 0, t_u)))
cube("D2'.svg",
     (arrow_left_shape, t_f),
     (arrow_left_shape, t_r))

cube("R'.svg",
     (arrow_down_shape, translate(3, 0, t_f)))
cube("L'.svg",
     (arrow_up_shape, t_f))
cube("U'.svg",
     (arrow_right_shape, translate(0, 3, t_f)))
cube("F'.svg",
     (arrow_up_shape, t_r))
cube("B'.svg",
     (arrow_down_shape, translate(3, 0, t_r)))
cube("D'.svg",
     (arrow_left_shape, t_f))

cube("Rs.svg",
     (arrow_up_shape, translate(2, 0, t_f)))
cube("Ls.svg",
     (arrow_down_shape, translate(1, 0, t_f)))
cube("Us.svg",
     (arrow_left_shape, translate(0, 2, t_f)))
cube("Fs.svg",
    (arrow_down_shape, translate(1,0, t_r)))
cube("Bs.svg",
    (arrow_up_shape, translate(2, 0, t_r)))
cube("Ds.svg",
    (arrow_right_shape, translate(0, 1, t_f)))

cube("Rs'.svg",
     (arrow_down_shape, translate(2, 0, t_f)))
cube("Ls'.svg",
     (arrow_up_shape, translate(1, 0, t_f)))
cube("Us'.svg",
     (arrow_right_shape, translate(0, 2, t_f)))
cube("Fs'.svg",
     (arrow_up_shape, translate(1, 0, t_r)))
cube("Bs'.svg",
     (arrow_down_shape, translate(2, 0, t_r)))
cube("Ds'.svg",
     (arrow_left_shape, translate(0, 1, t_f)))

cube("Rs2.svg",
     (arrow_up_shape, translate(2, 0, t_f)),
     (arrow_up_shape, translate(2, 0, t_u)))
cube("Ls2.svg",
     (arrow_down_shape, translate(1, 0, t_f)),
     (arrow_down_shape, translate(1, 0, t_u)))
cube("Us2.svg",
     (arrow_left_shape, translate(0, 2, t_f)),
     (arrow_left_shape, translate(0, 2, t_r)))
cube("Fs2.svg",
     (arrow_down_shape, translate(1, 0, t_r)),
     (arrow_right_shape, translate(0, 1, t_u)))
cube("Bs2.svg",
     (arrow_up_shape, translate(2, 0, t_r)),
     (arrow_left_shape, translate(0, 2, t_u)))
cube("Ds2.svg",
     (arrow_right_shape, translate(0, 1, t_f)),
     (arrow_right_shape, translate(0, 1, t_r)))

cube("Rs2'.svg",
     (arrow_down_shape, translate(2, 0, t_f)),
     (arrow_down_shape, translate(2, 0, t_u)))
cube("Ls2'.svg",
     (arrow_up_shape, translate(1, 0, t_f)),
     (arrow_up_shape, translate(1, 0, t_u)))
cube("Us2'.svg",
     (arrow_right_shape, translate(0, 2, t_f)),
     (arrow_right_shape, translate(0, 2, t_r)))
cube("Fs2'.svg",
     (arrow_up_shape, translate(1, 0, t_r)),
     (arrow_left_shape, translate(0, 1, t_u)))
cube("Bs2'.svg",
     (arrow_down_shape, translate(2, 0, t_r)),
     (arrow_right_shape, translate(0, 2, t_u)))
cube("Ds2'.svg",
     (arrow_left_shape, translate(0, 1, t_f)),
     (arrow_left_shape, translate(0, 1, t_r)))


cube("RW.svg",
    (arrow_up_shape, translate(2, 0, t_f)),
    (arrow_up_shape, translate(3, 0, t_f)),)
cube("LW.svg",
    (arrow_down_shape, t_f),
    (arrow_down_shape, translate(1, 0, t_f)))
cube("UW.svg",
     (arrow_left_shape, translate(0, 2, t_f)),
     (arrow_left_shape, translate(0, 3, t_f)))
cube("FW.svg",
     (arrow_down_shape, t_r),
     (arrow_down_shape, translate(1, 0, t_r)))
cube("BW.svg",
     (arrow_up_shape, translate(3, 0, t_r)),
     (arrow_up_shape, translate(2, 0, t_r)))
cube("DW.svg",
     (arrow_right_shape, t_f),
     (arrow_right_shape, translate(0, 1, t_f)))

cube("RW2.svg",
    (arrow_up_shape, translate(2, 0, t_f)),
    (arrow_up_shape, translate(3, 0, t_f)),
    (arrow_up_shape, translate(2, 0, t_u)),
    (arrow_up_shape, translate(3, 0, t_u)))
cube("LW2.svg",
    (arrow_down_shape, t_f),
    (arrow_down_shape, translate(1, 0, t_f)),
    (arrow_down_shape, t_u),
    (arrow_down_shape, translate(1, 0, t_u)))
cube("UW2.svg",
     (arrow_left_shape, translate(0, 2, t_f)),
     (arrow_left_shape, translate(0, 3, t_f)),
     (arrow_left_shape, translate(0, 2, t_r)),
     (arrow_left_shape, translate(0, 3, t_r)))
cube("FW2.svg",
     (arrow_down_shape, t_r),
     (arrow_down_shape, translate(1, 0, t_r)),
     (arrow_right_shape, t_u),
     (arrow_right_shape, translate(0, 1, t_u)))
cube("BW2.svg",
     (arrow_up_shape, translate(3, 0, t_r)),
     (arrow_up_shape, translate(2, 0, t_r)),
     (arrow_left_shape, translate(0, 3, t_u)),
     (arrow_left_shape, translate(0, 2, t_u)))
cube("DW2.svg",
     (arrow_right_shape, t_f),
     (arrow_right_shape, translate(0, 1, t_f)),
     (arrow_right_shape, t_r),
     (arrow_right_shape, translate(0, 1, t_r)))

cube("RW'.svg",
    (arrow_down_shape, translate(2, 0, t_f)),
    (arrow_down_shape, translate(3, 0, t_f)))
cube("LW'.svg",
    (arrow_up_shape, t_f),
    (arrow_up_shape, translate(1, 0, t_f)))
cube("UW'.svg",
     (arrow_right_shape, translate(0, 2, t_f)),
     (arrow_right_shape, translate(0, 3, t_f)))
cube("FW'.svg",
     (arrow_up_shape, t_r),
     (arrow_up_shape, translate(1, 0, t_r)))
cube("BW'.svg",
     (arrow_down_shape, translate(3, 0, t_r)),
     (arrow_down_shape, translate(2, 0, t_r)))
cube("DW'.svg",
     (arrow_left_shape, t_f),
     (arrow_left_shape, translate(0, 1, t_f)))

cube("X.svg",
    (arrow_up_shape, t_f),
    (arrow_up_shape, translate(1, 0, t_f)),
    (arrow_up_shape, translate(2, 0, t_f)),
    (arrow_up_shape, translate(3, 0, t_f)))

cube("X2.svg",
    (arrow_up_shape, t_f),
    (arrow_up_shape, translate(1, 0, t_f)),
    (arrow_up_shape, translate(2, 0, t_f)),
    (arrow_up_shape, translate(3, 0, t_f)),
    (arrow_up_shape, t_u),
    (arrow_up_shape, translate(1, 0, t_u)),
    (arrow_up_shape, translate(2, 0, t_u)),
    (arrow_up_shape, translate(3, 0, t_u)))

cube("X'.svg",
     (arrow_down_shape, t_f),
     (arrow_down_shape, translate(1, 0, t_f)),
     (arrow_down_shape, translate(2, 0, t_f)),
     (arrow_down_shape, translate(3, 0, t_f)))

cube("Y.svg",
    (arrow_left_shape, t_f),
    (arrow_left_shape, translate(0, 1, t_f)),
    (arrow_left_shape, translate(0, 2, t_f)),
    (arrow_left_shape, translate(0, 3, t_f)))

cube("Y2.svg",
    (arrow_left_shape, t_f),
    (arrow_left_shape, translate(0, 1, t_f)),
    (arrow_left_shape, translate(0, 2, t_f)),
    (arrow_left_shape, translate(0, 3, t_f)),
    (arrow_left_shape, t_r),
    (arrow_left_shape, translate(0, 1, t_r)),
    (arrow_left_shape, translate(0, 2, t_r)),
    (arrow_left_shape, translate(0, 3, t_r)))

cube("Y'.svg",
    (arrow_right_shape, t_f),
    (arrow_right_shape, translate(0, 1, t_f)),
    (arrow_right_shape, translate(0, 2, t_f)),
    (arrow_right_shape, translate(0, 3, t_f)))

cube("Z.svg",
     (arrow_up_shape, t_r),
     (arrow_up_shape, translate(1, 0, t_r)),
     (arrow_up_shape, translate(2, 0, t_r)),
     (arrow_up_shape, translate(3, 0, t_r)))

cube("Z2.svg",
     (arrow_up_shape, t_r),
     (arrow_up_shape, translate(1, 0, t_r)),
     (arrow_up_shape, translate(2, 0, t_r)),
     (arrow_up_shape, translate(3, 0, t_r)),
     (arrow_left_shape, t_u),
     (arrow_left_shape, translate(0, 1, t_u)),
     (arrow_left_shape, translate(0, 2, t_u)),
     (arrow_left_shape, translate(0, 3, t_u)))

cube("Z'.svg",
     (arrow_down_shape, t_r),
     (arrow_down_shape, translate(1, 0, t_r)),
     (arrow_down_shape, translate(2, 0, t_r)),
     (arrow_down_shape, translate(3, 0, t_r)))
