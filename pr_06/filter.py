from PIL import Image, ImageDraw
import numpy as np
class MyImage:
    F = 0.0625
    # F = 0.03125
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.input_pixels = self.image.load()
        self.output_image = Image.new("RGB", self.image.size)
        self.draw = ImageDraw.Draw(self.output_image)
        self.width = self.image.width
        self.height = self.image.height
    
    def conv_gauss_blur(self, kernel_matrix=(np.array([[1,2,1],[2,4,2],[1,2,1]])*F)):
        # Middle of the kernel
        offset = len(kernel_matrix) // 2
        # Compute convolution between intensity and kernels
        for x in range(offset, self.image.width - offset):
            for y in range(offset, self.image.height - offset):
                acc = [0, 0, 0]
                for a in range(len(kernel_matrix)):
                    for b in range(len(kernel_matrix)):
                        xn = x + a - offset
                        yn = y + b - offset
                        pixel = self.input_pixels[xn, yn]
                        acc[0] += pixel[0] * kernel_matrix[a][b]
                        acc[1] += pixel[1] * kernel_matrix[a][b]
                        acc[2] += pixel[2] * kernel_matrix[a][b]
                self.draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
        self.output_image.show()
        self.output_image.save("gaussian_blur_output1.png")
    def dilation(self, kernel_matrix=(np.array([[0,1,0],[1,1,1],[0,0,0]])*F)):
        # Middle of the kernel
        offset = len(kernel_matrix) // 2
        # Compute convolution between intensity and kernels
        for x in range(offset, self.image.width - offset):
            for y in range(offset, self.image.height - offset):
                current_px_color = self.input_pixels[x, y]
                acc = [0, 0, 0]
                temp_acc_r = []
                temp_acc_g = []
                temp_acc_b = []
                for a in range(len(kernel_matrix)):
                    for b in range(len(kernel_matrix)):
                        xn = x + a - offset
                        yn = y + b - offset
                        pixel = self.input_pixels[xn, yn]
                        acc[0] += pixel[0] + kernel_matrix[a][b]
                        acc[1] += pixel[1] + kernel_matrix[a][b]
                        acc[2] += pixel[2] + kernel_matrix[a][b]
                        temp_acc_r.append(acc[0])
                        temp_acc_g.append(acc[1])
                        temp_acc_b.append(acc[2])
                self.draw.point((x, y), (int(max(temp_acc_r)+current_px_color[0]), int(max(temp_acc_g)+current_px_color[1]), int(max(temp_acc_b)+current_px_color[2])))
        self.output_image.show()
        self.output_image.save("dilation_output111.png")
    def erosion(self, kernel_matrix=(np.array([[0,1,0],[1,1,1],[0,0,0]])*F)):
        # Middle of the kernel
        offset = len(kernel_matrix) // 2
        # Compute convolution between intensity and kernels
        for x in range(offset, self.image.width - offset):
            for y in range(offset, self.image.height - offset):
                current_px_color = self.input_pixels[x, y]
                acc = [0, 0, 0]
                temp_acc_r = []
                temp_acc_g = []
                temp_acc_b = []
                for a in range(len(kernel_matrix)):
                    for b in range(len(kernel_matrix)):
                        xn = x + a - offset
                        yn = y + b - offset
                        pixel = self.input_pixels[xn, yn]
                        acc[0] += pixel[0] - kernel_matrix[a][b]
                        acc[1] += pixel[1] - kernel_matrix[a][b]
                        acc[2] += pixel[2] - kernel_matrix[a][b]
                        temp_acc_r.append(acc[0])
                        temp_acc_g.append(acc[1])
                        temp_acc_b.append(acc[2])
                self.draw.point((x, y), (int(min(temp_acc_r)+current_px_color[0]), int(min(temp_acc_g)+current_px_color[1]), int(min(temp_acc_b)+current_px_color[2])))
        self.output_image.show()
        self.output_image.save("erosion_output111.png")

m = MyImage('img.jpeg')
# m.conv_gauss_blur()
m.dilation()
# m.erosion()
# m.conv_gauss_blur(np.array([[1,0,1],[2,0,-2],[1,0,1]]))