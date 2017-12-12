#!/usr/bin/env python
import sys
sys.path.append('/home/shoban')
from PIL import Image
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
# Function to display modal values based on cursor position
def format_coord(x, y):
    z=depth[int(y)][int(x)]*0.00470
    w=ir[int(y)][int(x)]*255
    x_m = (x-320)*0.00223
    y_m = (240-y)*0.00216+0.08
    return 'x=%1.4f, y=%1.4f,x_m=%1.4f, y_m=%1.4f, depth=%1.4f, ir=%1.4f'%(x,y,x_m,y_m,z,w)


p = sys.argv[4]
print(p)
# Getting the input Images from different modalities
im1=Image.open(sys.argv[1])
im2=Image.open(sys.argv[2])
im3=Image.open(sys.argv[3])
im3=im3.convert('L')
depth = mpimg.imread(im3)
depth = rgb2gray(depth) * 255
ir = mpimg.imread(im2)


im1.save('C:/Python27/1.png','PNG')
im1=im1.convert('L')

#im2=im2.convert('L')
# Resizing to frame size of Realsense
im1=im1.resize((640,480))
im2=im2.point(lambda i: i*4)
#im2=im2.point(lambda i: i+80)
im2.save('C:/Python27/2.png','PNG')
# Displaying Image based on the combination of modalities given as input
if(p=='1'):
	result=Image.blend(im1,im2,0.5)
elif(p=='2'):
	result=Image.blend(im1,im3,0.5)
elif(p=='3'):
	result=Image.blend(im3,im2,0.5)
else:
	result=Image.blend(im1,im2,0.5)
# Blending the combination of modalities
	result=Image.blend(result,im3,0.5)

result.save('C:/Python27/hyperspectral.png','PNG')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(result2)

ax.format_coord = format_coord
plt.axes()
plt.show()
