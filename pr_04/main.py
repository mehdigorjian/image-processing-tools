from pixel import Pixel   
from curve import Curve
from PIL import Image, ImageDraw
from utility import rgb_to_hsv, hsv_to_rgb, image_manipulation

def main():
    
    # 1st part: drawing curve and manipulate image color
    input_image = Image.open('zzz.jpg')
    pp0 = Pixel(30,30)
    pp1 = Pixel(330,30)
    C = Curve(input_image)
    cc = C.curve_draw(pp0, pp1, [(.2,90), (.4, 350), (.6, 100), (.8, 80)])
    # cc = C.curve_draw(pp0, pp1, [(.2,90), (.4, 150), (.6, 100), (.8, 80)])
    # cc = C.curve_draw(pp0, pp1, [(.2,70), (.4, 100), (.6, 120), (.8, 80)])
    # cc = C.curve_draw(pp0, pp1, [(.2,90), (.4, 120), (.6, 100), (.8, 80)])
    C.image.show()
    print(cc)
    a, b, c = C.calc_parabola_vertex(int(cc[1][0]),int(cc[1][1]), int(cc[2][0]),int(cc[2][1]),int(cc[3][0]),int(cc[3][1]))
    C.color_map(a,b,c)
    C.image.show()
    print(a, b,c)
    
    # 2nd part: hue switching
    image_manipulation('zzz.jpg', 'Second_Image.png', save_name='hue_modification.png')
    image_manipulation('zzz.jpg', 'Second_Image_1.png', save_name='hue_modification_1.png')
    image_manipulation('zzz.jpg', 'Second_Image_2.png', save_name='hue_modification_2.png')

if __name__ == '__main__':
    main()