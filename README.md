# image_processing_application
Creating an application to manipulate raster images
## project_01: Create-Display-Read & Write color images
  1. Your first program should be able to read a file that can be considered a PPM image, i.e. it has to have an ASCII header that describe image properties like a PPM file. Your program should be able to read and use it to display an image.
  2. In the second program you will create your own image procedurally and display it in your program. You should also be able to write this procedurally created image into PPM file format. If everything works correctly, the first program should be able to read and display this file.
  3. Your program can create other images and we can give you bonus credit for additional work. Put your resulting images to your website. Do not use any high level operation such as ``read PPM''. For the required parts of the project, implement your operations only using the basic programming operations.
## project_02: Simple Vector to Raster Conversion and Antializing
  1. Your program(s) should create at least one half-plane, one circle, a shape defined by a function in the form of f(x,y)<0. You can choose any color and any shape. We also want to see close-up images that demonstrate that the antialising is working.
## project_03: Complex Vector to Raster Conversion
  1. Your program(s) should create at least one convex, one star shape, one blobby shape and one shaded shape. In addition, create a height field image defined by a function in the form of y=f(x). You can choose any color and any shape. We also want to see close-up images that demonstrate that the antialising is working.
## project_04: Image Manipulations
  The three tasks in this case are the following. Our goal is to implement something that you cannot create by using commercial software. In each case, provide start with a standard approach and create your own using an unconventional input such an image.

  1. Manipulate colors in an image using an interpolating curve. Curve parameters will be given as a list of numbers such as (r0,r1,r2,r3...,rn) which means a parametric curve that passes through from points (0,r0), (1/n,r1), (2/n,r2), (3/n,r3) and (1,rn). We suggest to start with piecewise-linear curve and extend to hermitian cubics later. If you finish piecewise-linear, you will get full credit.
  2. Replace Hues in an image taking hues from another image. For the information about how to compute hues, see below.
## project_05: Basic Convolution Filters
You are supposed to implement three of the following filters to get the full credit. Each one of the is equally weighted.
  1. Convolution filter with Partition of Unity Property: These are fileters such blur or motion blur. In this case, coefficients of filter kernels add up to one.
  2. Derivative type Filters: These are filters when applied to a constant image gives 0. In this case, direct application of convolution filters can give you negative numbers. Therefore, in this case, we need to make one more conversion to obtain an image consists of colors, i.e. positive numbers.
  3. Morphological filters: Dilation and/or Erosion filter.
## project_06: Filtering with Non-stationary Kernels
You are supposed to implement two of the following filters to get the full credit. Each one of the is equally weighted.
  1. Convolution filter - Motion Blur. In this case the direction and the size of the motion blur will be controlled by a vector field. (A Simple way of creating a vector field is to use an image. For instance, red and green channels of an image can be converted into x,y by a simple linear transformation.). This will give you look of Line Integral Convolution.
  2. Morphological Non-Stationary filter - In this case the size and shape of the Dilation and/or Erosion filter will be controlled by another image.
## project_07: Transformations and Warping
You are supposed to implement following methods to get the full credit. Each one of the is equally weighted. To get the credit, your results must not have unwanted artifacts such as holes. To avoid these artifacts, you will need to use inverse mapping along with antialasing techniques you used before.
  1. Linear Transformations that can be done by 2x2 matrices: Rotation, Scaling, Shear, Mirror
  2. Transformations that require 3x3 matrices: Translation and Perspective
  2. Bilinear warping
## project_08: Compositing
  1. Compositing two images with alpha maps: Implement Over operation (called normal in Photoshop), Multiplication,Substraction and Max/Min.
  2. Develop a Blue/Green Screening tailored for a specific image. In this case, the goal is to construct an alpha map that can provide an acceptable blue-screening result for a given image.
## project_09: Dithering and Screening
You are supposed to implement following methods to get the full credit. Each one of the is equally weighted.
  1. Floyd-Steinberg Error diffusion
  2. An Ordered Dither
## project_10: Stiching and Carving
You are supposed to develop the following two software to get the full credit. Each one of the is equally weighted.
  1. Image Recombination: A software that can seamlessly combine two similar images into one. Your algorithm will find the best seam that can go through both of the images. Using this seam, your program will combine the two images into one such that one side of the final image will come from first image and other side will come from second image.
  2. Image Retargeting by Seam Carving: A software that can change the size of the image by removing least energy seams.
## project_11: 2D Diffuse Shader
You will implement a local illumination shader and turn one of your previous works into video processing. We will show the final video in semester end-show, therefore the idea must be something that can get aesthetic video results.
  1. Video Processing: Turn one of your previous works into video processing. Your program must be able to take an few input videos, that can be given a set of images. From these videos, it will create a final video to be shown semester end show.
  2. Diffuse (Lambertian) Illumination Shader: You will read a normal map image and illuminate it with a light source. You will only use basic shading with diffuse reflections. Shader will be described by two color texture images instead of single color: diffuse and ambient. You will make an animation by moving the light source direction or position.
  3. Specular Highlight Shader: You will add specular highlights to your diffuse shader. Shader will be described by three color texture images instead of single color: diffuse, ambient and specular. You will make an animation by moving the light source direction or position.
## project_12: 2D Reflection & Refraction Shader
You will implement a simple global shader.
  1. Reflection Shader: A normal map will reflect a foreground image. You will animate by moving texture.
  2. Refraction Shader: A normal map will refract a background image. You will animate by either moving texture or changing index of refraction.
  3. Fresnel Shader: You will combine reflection and refraction using Fresnel.
