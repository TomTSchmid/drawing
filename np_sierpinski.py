from PIL import Image
import numpy as np
import math
import random

# img_w, img_h = 500, 500
img_w, img_h = 1440, 3168
data = np.zeros((img_h, img_w, 3), dtype=np.uint8)

size = 1400
xOffset = (img_w-size)/2
yOffset = 1200
iterations = 500000
# corners = 3
# winkel = np.radians(360/6)

# colors = ["green", "blue", "purple", "red", "orange", "yellow"]

# data[10:80, 10:80] = [255, 0, 0]
# data[img_w-10:img_w-80, 10:80] = [0, 255, 0]

# for i in range(img_w-1):
#      for j in range(img_h-1):
#           # data[i, j] = [i%255, j%255, (i+j)%255]
#           data[j, i] = [i%255, j%255, (i+j)%255]



p = [[img_w/2, yOffset],
     [img_w-xOffset, yOffset+math.cos(math.radians(30))*size],
     [xOffset, yOffset+math.cos(math.radians(30))*size]]

pos = p[1]

for i in range(iterations):
     r = random.randint(0, 2)
     x, y = round((pos[0]+p[r][0])/2), round((pos[1]+p[r][1])/2)
     data[y, x] = [0, 255, 0]
     pos = [x, y]
     
#     for j in range(1, 7):
#     # for j in range(6):
#         turtle.color(colors[j-1])
#         xshift = x*math.cos(winkel*j) - y*math.sin(winkel*j)
#         yshift = x*math.sin(winkel*j) + y*math.cos(winkel*j)
#         turtle.setpos(xshift, yshift)
#         turtle.dot(1.6)

# data2 = np.zeros

# hexagon
# p = [[size/2, 0],
#      [np.sin(np.radians(150))*size, np.cos(np.radians(150))*size],
#      [np.sin(np.radians(210))*size, np.cos(np.radians(210))*size]]

img = Image.fromarray(data, 'RGB')
img.save('pic_01.png')
