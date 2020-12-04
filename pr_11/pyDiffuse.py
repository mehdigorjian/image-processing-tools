from math import cos, sqrt
from PIL import Image, ImageDraw
import pygame
t0, t1 = .10, .80
s0, s1 = .10, .80
c2 = (0.1, 0.05, 0.05)
# L = (.50, .10, .50)
L = (.70, .10, .50)
# z = .5

n_img = pygame.image.load('oct.png')
w = n_img.get_width()
h = n_img.get_height()
W, H = w//5, h//5
n_img = pygame.transform.scale(n_img, (W, H))
output_image = pygame.Surface((W, H))
c0_img = pygame.image.load('black.png')
c0_img = pygame.transform.scale(c0_img, (W,H))
c1_img = pygame.image.load('white.png')
c1_img = pygame.transform.scale(c1_img, (W,H))

pygame.init()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Render')
clock = pygame.time.Clock()
mouse_X, mouse_Y = 10, 20

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

def getpixel_bound(image, a, b):
    x = 2 * (image.get_at((a,b))[0]/255) - 1
    y = 2 * (image.get_at((a,b))[1]/255) - 1
    z = 2 * (image.get_at((a,b))[2]/255) - 1
    return (x, y, z)

def control():
    global L, mouse_X, mouse_Y
    for i in range(W):
        for j in range(H):
            # print('X: ', mouse_X, 'Y: ', mouse_Y)
            d = sqrt( (mouse_X - i)**2 + (mouse_Y - j)**2 + L[2]**2 )
            if d == 0: d = .01
            L = ( (mouse_X - i)/d, (mouse_Y - j)/d, L[2]/d )
            
            t_temp = compute_t(getpixel_bound(n_img, i,j), L)
            s_temp = compute_s(getpixel_bound(n_img, i,j), L)

            cr_temp = c0_img.get_at((i,j))[0]/255 * (1 - t_temp) + c1_img.get_at((i,j))[0]/255 * t_temp
            cg_temp = c0_img.get_at((i,j))[1]/255 * (1 - t_temp) + c1_img.get_at((i,j))[1]/255 * t_temp
            cb_temp = c0_img.get_at((i,j))[2]/255 * (1 - t_temp) + c1_img.get_at((i,j))[2]/255 * t_temp

            cr = int((cr_temp * (1 - s_temp) + c2[0]) * 255)
            cg = int((cg_temp * (1 - s_temp) + c2[1]) * 255)
            cb = int((cb_temp * (1 - s_temp) + c2[2]) * 255)
            if cr < 0 : cr = 0
            if cg < 0 : cg = 0
            if cb < 0 : cb = 0
            if cr > 255: cr = 255
            if cg > 255: cg = 255
            if cb > 255: cb = 255
            output_image.set_at((i,j), (cr, cg, cb))
    win.blit(output_image, (0,0))
    pygame.image.save(output_image, 'output_diffuse5.png')

def redraw():
    win.fill((0,0,0))
    control()
    pygame.display.update()
    clock.tick(30)

def main_loop():
    global mouse_X, mouse_Y
    # win.fill((0,0,0))
    # control()
    action = True
    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_X, mouse_Y = pygame.mouse.get_pos()
                # print('X: ', mouse_X, ',', 'Y: ', mouse_Y)
        redraw()
        # control()
        # pygame.display.update()
        # clock.tick(30)

main_loop()