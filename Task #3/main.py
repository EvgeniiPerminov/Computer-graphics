from tools.affine_transformation import to_proj_coords, shift_mx, rotation_mx, diag_mx, to_cart_coords
from tools.bresenham import bresenham
from tools.parse import parse_obj_file

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'


obj_path = 'source/teapot.obj'
vertexes, faces = parse_obj_file(obj_path)
vertexes -= vertexes.sum(axis=0) / vertexes.shape[0]

im_size = (2000, 2000)
img_center = np.int_(np.array(im_size) // 2)
vertexes[:, 1] *= -1
vertexes = np.int_(vertexes[:, :2] * 100) + img_center
x_proj = to_proj_coords(vertexes.T)


N = 100
N_2 = N // 2

frames = []
fig = plt.figure(figsize=(10, 10))
T = shift_mx(-img_center)
img = np.zeros((*im_size, 3), dtype=np.uint8)

for i in range(N):
    img[:, :] = 0
    R = rotation_mx(i * 2 * np.pi / N_2)
    A = diag_mx(1 + i / N_2 if i < N_2 else 2 - i % N_2 / N_2)
    x_proj_new = np.linalg.inv(T) @ A @ R @ T @ np.copy(x_proj)
    x_new = np.int_(to_cart_coords(x_proj_new).T)

    r = np.abs(255 - i * 255 / N_2)
    g = i * 255 / N_2 if i < N_2 else 255 - i % N_2 * 255 / N_2
    cur_color = np.array([r, g, 0], dtype=np.uint8)

    for v1, v2, v3 in faces:
        bresenham(img, cur_color, *x_new[v1], *x_new[v2])
        bresenham(img, cur_color, *x_new[v1], *x_new[v3])
        bresenham(img, cur_color, *x_new[v2], *x_new[v3])

    frames.append([plt.imshow(img)])

ani = animation.ArtistAnimation(fig, frames, interval=40, blit=True, repeat_delay=0)
writer = PillowWriter(fps=24)
ani.save("teapot.gif", writer=writer)

