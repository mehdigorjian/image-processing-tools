import pygame
import numpy


def blend_texture_add(surface1_, surface2_, set_alpha1_, set_alpha2_, mask_=True, type='normal'):
    w, h = surface1_.get_width(), surface1_.get_height()
    buffer1 = surface1_.get_view('3')
    buffer2 = surface2_.get_view('3')
    alpha1_ = numpy.array(surface1_.get_view('a'), dtype=numpy.uint8).transpose(1, 0) / 255
    mask_alpha1 = alpha1_ <= 0
    alpha1 = numpy.full((w, h, 1), set_alpha1_).transpose(1, 0, 2)
    alpha2 = numpy.full((w, h, 1), set_alpha2_).transpose(1, 0, 2)
    rgb1 = (numpy.array(buffer1, dtype=numpy.uint8).transpose(1, 0, 2) / 255) #* alpha1
    rgb2 = (numpy.array(buffer2, dtype=numpy.uint8).transpose(1, 0, 2) / 255) #* alpha2
    new = numpy.zeros((w, h, 4))

    f = numpy.ones(rgb1.shape)

    if type == 'normal':
        f = rgb1
    elif type == 'multiply':
        f = numpy.multiply(rgb1, rgb2)
    elif type == 'subtract':
        f = numpy.absolute(numpy.subtract(rgb2, rgb1))
    elif type == 'min':
        f = numpy.minimum(rgb1, rgb2)
    elif type == 'max':
        f = numpy.maximum(rgb1, rgb2)

    new[:, :, :3] = numpy.add(rgb2 * f, rgb1 * (1 - alpha2))
    new[:, :, 3] = numpy.add(alpha2, alpha1 * (1 - alpha2)).reshape(w, h)

    new = numpy.multiply(new, 255)
    numpy.putmask(new, new > 255, 255)
    if mask_:
        new[mask_alpha1] = 0
    return pygame.image.frombuffer(new.copy('C').astype(numpy.uint8),(w, h), 'RGBA')


pygame.init()
SIZE = (300, 300)
screen = pygame.display.set_mode(SIZE)
screen.fill((0,0,0))
surface1 = pygame.image.load('background1.jpg').convert_alpha()
surface1 = pygame.transform.smoothscale(surface1, SIZE)

surface2 = pygame.image.load('foreground1.png').convert_alpha()
surface2 = pygame.transform.smoothscale(surface2, SIZE)
surface1_mask, surface2_mask = 1.0, 1.0

texture = blend_texture_add(surface1, surface2, surface1_mask, surface2_mask, mask_=True, type='normal')
pygame.image.save(texture, 'blend_normal1.png')

# normal
# texture = blend_texture_add(surface1, surface2, surface1_mask, surface2_mask, mask_=True, type='multiply')
# pygame.image.save(texture, 'blend_multiply.png')

# subtract
# texture = blend_texture_add(surface1, surface2, surface1_mask, surface2_mask, mask_=True, type='subtract')
# pygame.image.save(texture, 'blend_subtract.png')

# min
# texture = blend_texture_add(surface1, surface2, surface1_mask, surface2_mask, mask_=True, type='min')
# pygame.image.save(texture, 'blend_min.png')

# max
# texture = blend_texture_add(surface1, surface2, surface1_mask, surface2_mask, mask_=True, type='max')
# pygame.image.save(texture, 'blend_max.png')

action = True
while action:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False
    screen.blit(texture, (0, 0))
    pygame.display.update()