from tools.bresenham import bresenham
from tools.parse import parse_obj_file
import matplotlib.pyplot as plt
import numpy as np


obj_path = 'source/teapot.obj'
vertexes, faces = parse_obj_file(obj_path)

im_size = (1000, 1000)

img_center = np.array(im_size) // 2
vertexes[:, 1] *= -1
vertexes = np.int_(vertexes[:, :2] * 100) + img_center


fig = plt.figure(figsize=(10, 10))
img = np.zeros((*im_size, 3), dtype=np.uint8)
color = np.array([255, 255, 255])


for v1, v2, v3 in faces:
    bresenham(img, color, *vertexes[v1], *vertexes[v2])
    bresenham(img, color, *vertexes[v1], *vertexes[v3])
    bresenham(img, color, *vertexes[v2], *vertexes[v3])

plt.imsave('teapot.png', img)
plt.imshow(img)
plt.show()
