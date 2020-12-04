from PIL import Image, ImageDraw
MAX_ITER = 80
import math, random
# Image size (pixels)
WIDTH = 350
HEIGHT = 200
# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1
palette = []

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))

        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        # color = 255 - int(m * 255 / MAX_ITER)
        color1 = 2 - int(m * math.sin(255/ MAX_ITER))
        color2 = 10 - int(m * math.cos(255/ MAX_ITER))
        color3 = 5 - int(math.sin(255/ MAX_ITER))

        # Plot the point
        # draw.point([x, y], (color1, color2, color3))

        if x%3 ==0:
            draw.point([x+random.randint(0, 100), y], (color3, color2, color1))
        else:
            draw.point([x, y], (color1, color2, color3))


im.save('output1.png', 'PNG')
im.show('output1.png')