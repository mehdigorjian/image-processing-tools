import pygame
import numpy as np
def alpha_blending(_surface1, _surface2):
    assert isinstance(_surface1, pygame.Surface), 'Expected Surface got {_surface1}'
    assert isinstance(_surface2, pygame.Surface), 'Expected Surface got {_surface2}'

    w, h = _surface1.get_size()

    buf1 = _surface1.get_view('3')
    buf2 = _surface2.get_view('3')

    rgb1 = np.array(buf1, dtype=np.uint8).transpose(1,0,2)/255
    rgb2 = np.array(buf2, dtype=np.uint8).transpose(1,0,2)/255

    new = np.zeros((w, h, 4))

    alpha1 = (np.array(_surface1.get_view('a'), dtype=np.uint8).transpose(1,0)).reshape(w,h,1)/255
    alpha2 = (np.array(_surface2.get_view('a'), dtype=np.uint8).transpose(1,0)).reshape(w,h,1)/255

    for i in range(w):
        for j in range(h):
            alpha = alpha1[i][j] + alpha2[i][j] *(1 - alpha1[i][j])
            assert alpha > 0, 'ZeroDivision'
            rgb = (rgb1[i][j] * alpha1[i][j] + rgb2[i][j] * alpha2[i][j] * (1 - alpha1[i][j])) / alpha
            new[i][j] = (*rgb, alpha)
    
    new = np.multiply(new, 255)
    return pygame.image.frombuffer(new.copy('C').astype(np.uint8),(w, h), 'RGBA')


pygame.init()
SIZE = (300, 300)
screen = pygame.display.set_mode(SIZE, 0, 32)

# np.set_printoptions(threshold=np.nan)
screen.fill((0,0,0))
surface1 = pygame.image.load('background1.jpg').convert_alpha()
surface1 = pygame.transform.scale(surface1, SIZE)

surface2 = pygame.image.load('foreground1.png').convert_alpha()
surface2 = pygame.transform.scale(surface2, SIZE)
# texture = alpha_blending(surface1, surface2)

# pygame.image.save(texture, 'Blend.png')

action = True
while action:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False
    texture = alpha_blending(surface1, surface2)
    screen.blit(texture, (0, 0))
    pygame.display.update()