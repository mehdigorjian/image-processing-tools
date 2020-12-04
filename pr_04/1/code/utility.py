import math
from PIL import Image, ImageDraw
def rgb_to_hsv(rgb_color):
    r, g, b = rgb_color
    h, s, v = 0, 0, 0
    red = r / 255.0 
    green = g / 255.0
    blue = b / 255.0
    max1 = max(red, green, blue)
    min1 = min(red, green, blue)    
    v = max1 
    if max1 == 0:
        s = 0
        h = 0
    else:
        s = (max1 - min1) / max1
        delta = max1 - min1
        if delta == 0: h = 0
        else:
            if red == max1:            
                h = 60 * ((green - blue) / delta)
            elif green == max1:
                h = 60 * (2.0 + (blue - red) / delta)
            else:
                if h < 0: h = h + 360.0
                else: h = 60 * (4.0 + (red - green) / delta)
    return (h, s, v)

def hsv_to_rgb(hsv_color):
    r, g, b = 0, 0, 0
    h, s, v = hsv_color
    if h == 0.0: h == 360.0
    else: h /= 60.0
    fract = h - math.floor(h)
    P = v * (1.0 - s)
    Q = v * (1.0 - s * fract)
    T = v * (1.0 - s * (1.0 - fract))
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
def image_manipulation(_image1, _image2, save_name):
    image1 = Image.open(_image1)
    image2 = Image.open(_image2)

    for i in range(image1.width):
        for j in range(image1.height):
            im1_pix = image1.getpixel((i,j))
            h1, _, _ = rgb_to_hsv(im1_pix)

            im2_pix = image2.getpixel((i,j))
            _, s2, v2 = rgb_to_hsv(im2_pix)

            rr, gg, bb = hsv_to_rgb((h1, s2, v2))
            image2.putpixel((i,j), (rr, gg, bb))
    image2.show(title='im2')
    image2.save(save_name, 'PNG')