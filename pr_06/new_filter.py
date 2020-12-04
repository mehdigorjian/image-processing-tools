from PIL import Image, ImageDraw
import numpy as np
import math
from tqdm import tqdm
class MyImage:

    def __init__(self, image_path, img_integral_path):
        self.image = Image.open(image_path)
        self.img_intg = Image.open(img_integral_path)
        self.input_pixels = self.image.load()
        # self.output_image = Image.new("RGB", self.image.size)
        self.output_image = self.image.copy()
        self.draw = ImageDraw.Draw(self.output_image)
        self.width = self.image.width
        self.height = self.image.height

    def angle_calc(self, x, y):
        r_color, _, _ = self.img_intg.getpixel((x,y))
        return (1 - r_color/255) * math.pi

    def compute_kernel_matrix(self, x, y, kernel_shape):
        _offset = kernel_shape//2
        c = np.zeros((kernel_shape, kernel_shape))
        for i in range(0, kernel_shape):
            for j in range(0, kernel_shape):
                L = - math.sin(self.angle_calc(x,y)) * (i - _offset) + math.cos(self.angle_calc(x,y)) * (j - _offset)
                c[i, j] = math.exp(-L)
        sum = np.sum(c)
        # print(np.round(c/sum, decimals=1))
        return np.round(c / sum, decimals=1)
        # return c / sum

    def parametric_motion_blur(self, _kernel_shape=3):
        # Middle of the kernel
        offset = _kernel_shape//2
        # Compute convolution between intensity and kernels
        for x in tqdm(range(offset, self.image.width - offset)):
            for y in tqdm(range(offset, self.image.height - offset)):
                k_matrix = self.compute_kernel_matrix(x, y, _kernel_shape)
                acc = [0, 0, 0]
                for a in range(len(k_matrix)):
                    for b in range(len(k_matrix)):
                        xn = x + a - offset
                        yn = y + b - offset
                        pixel = self.input_pixels[xn, yn]
                        acc[0] += pixel[0] * k_matrix[a][b]
                        acc[1] += pixel[1] * k_matrix[a][b]
                        acc[2] += pixel[2] * k_matrix[a][b]
                self.draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))

        self.output_image.show()
        self.output_image.save("motion_blur_output20.png")

    def parametric_dilation(self, _kernel_shape):
        # Middle of the kernel
        offset = _kernel_shape // 2
        # Compute convolution between intensity and kernels
        for x in tqdm(range(offset, self.image.width - offset)):
            for y in tqdm(range(offset, self.image.height - offset)):
                k_matrix = self.compute_kernel_matrix(x, y, _kernel_shape)
                current_px_color = self.input_pixels[x, y]
                acc = [0, 0, 0]
                temp_acc_r = []
                temp_acc_g = []
                temp_acc_b = []
                for a in range(len(k_matrix)):
                    for b in range(len(k_matrix)):
                        xn = x + a - offset
                        yn = y + b - offset
                        pixel = self.input_pixels[xn, yn]
                        acc[0] += pixel[0] + k_matrix[a][b]
                        acc[1] += pixel[1] + k_matrix[a][b]
                        acc[2] += pixel[2] + k_matrix[a][b]
                        temp_acc_r.append(acc[0])
                        temp_acc_g.append(acc[1])
                        temp_acc_b.append(acc[2])
                self.draw.point((x, y), (int(max(temp_acc_r)+current_px_color[0]), int(max(temp_acc_g)+current_px_color[1]), int(max(temp_acc_b)+current_px_color[2])))
        self.output_image.show()
        self.output_image.save("parametric_dilation_output20.png")

m = MyImage('img.jpg', 'int_img.jpg')
# m.parametric_motion_blur(_kernel_shape=9)
m.parametric_dilation(_kernel_shape=3)