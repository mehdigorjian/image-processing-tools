import math
def hsv_to_rgb(hsv_color):
    r, g, b = 0, 0, 0
    h, s, v = hsv_color
    if h == 0.0: h == 360.0
    else: h /= 60.0
    fract = h - math.floor(h)
    P = v * (1. - s)
    Q = v * (1. - s * fract)
    T = v * (1. - s * (1. - fract))
    if h >= 0.0 and h < 1.0:
        r, g, b = v, T, P
    elif h >= 1.0 and h < 2.0:
        r, g, b = Q, v, P
    elif h >= 2.0 and h < 3.0:
        r, g, b = P, v, T
    elif h >= 3.0 and h < 4.0:
        r, g, b = P, Q, v
    elif h >= 4.0 and h < 5.0:
        r, g, b = T, P, v
    elif h >= 5.0 and h < 6.0:
        r, g, b = v, P, Q
    else:
        r, g, b = 0.0, 0.0, 0.0
    return (round(r * 255), round(g * 255), round(b * 255))

print(hsv_to_rgb((31.764, .607, .109)))