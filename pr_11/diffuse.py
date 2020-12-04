from math import cos
from PIL import Image, ImageDraw

t0, t1 = .10, .80
s0, s1 = .10, .80
c2 = (0.1, 0.05, 0.05)
# L = (.50, .10, .50)
L = (.70, .10, .50)


n_img = Image.open('oct.png')
output_image = Image.new("RGB", n_img.size)
c0_img = Image.open('black.png')
c0_img = c0_img.resize(n_img.size)
c1_img = Image.open('white.png')
c1_img = c1_img.resize(n_img.size)


def compute_t(N, L):
    t = L[0]*N[0] + L[1]*N[1] + L[2]*N[2]
    if (t - t0)/(t1 - t0) > 1: t = 1
    if (t - t0)/(t1 - t0) < 0: t = 0
    # print('t: ', t)
    return t

def compute_s(N, L):
    s = -L[2] + 2 * (L[0]*N[0] + L[1]*N[1] + L[2]*N[2]) * N[2]
    if (s - s0)/(s1 - s0) > 1: s = 1
    if (s - s0)/(s1 - s0) < 0: s = 0
    # print('s: ', s)
    return s

def getpixel_bound(image, x, y):
    x = 2 * (image.getpixel((x,y))[0]/255) - 1
    y = 2 * (image.getpixel((x,y))[1]/255) - 1
    z = 2 * (image.getpixel((x,y))[2]/255) - 1
    return (x, y, z)

for i in range(n_img.size[0]):
    for j in range(n_img.size[1]):
        t_temp = compute_t(getpixel_bound(n_img, i,j), L)
        s_temp = compute_s(getpixel_bound(n_img, i,j), L)

        cr_temp = c0_img.getpixel((i,j))[0]/255 * (1 - t_temp) + c1_img.getpixel((i,j))[0]/255 * t_temp
        cg_temp = c0_img.getpixel((i,j))[1]/255 * (1 - t_temp) + c1_img.getpixel((i,j))[1]/255 * t_temp
        cb_temp = c0_img.getpixel((i,j))[2]/255 * (1 - t_temp) + c1_img.getpixel((i,j))[2]/255 * t_temp

        cr = cr_temp * (1 - s_temp) + c2[0]
        cg = cg_temp * (1 - s_temp) + c2[1]
        cb = cb_temp * (1 - s_temp) + c2[2]

        output_image.putpixel((i,j), (int(cr*255), int(cg*255), int(cb*255)))

output_image.show()
output_image.save('output_diffuse4.png')