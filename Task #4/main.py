import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from tools.parse import parse_json_file
from tools.tools import thirdOrdBez, interRepr
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'


n_digits = 10
n_segments = 4
n_pointsins = 4
n_axles = 2


digits = parse_json_file('source/digits.json', (n_digits, n_segments, n_pointsins, n_axles))
digits -= np.int_(digits[0].sum(axis=0).sum(axis=0) / (n_segments * n_pointsins))

img_size = (1000, 1000)
digits += np.array(np.asarray(img_size) // 2, dtype=np.int32)

tr_steps = 20
third_order_bezier_steps = 100

tensor = np.zeros((n_digits, tr_steps, n_segments, third_order_bezier_steps, n_axles),
                  dtype=np.int32)

for tr in range(n_digits):
    for step, u in enumerate(np.linspace(0, 1, tr_steps)):
        for segment in range(n_segments):
            first_seg = digits[tr, segment]
            second_seg = digits[(tr + 1) % n_digits, segment]
            tensor[tr, step, segment] = thirdOrdBez(interRepr(first_seg, second_seg, u), third_order_bezier_steps)


frames = []
fig = plt.figure(figsize=(10, 10))
img = np.zeros((*img_size, 3), dtype=np.uint8)
color = np.array([255, 0, 191])


for tr in range(n_digits):
    for steps in range(tr_steps):
        img[:, :] = 0
        for segment in range(n_segments):
            for point in range(third_order_bezier_steps):
                x = tensor[tr, steps, segment, point][0]
                y = tensor[tr, steps, segment, point][1]
                img[y - 2: y + 2, x - 2: x + 2] = color

        frames.append([plt.imshow(img)])

ani = animation.ArtistAnimation(fig, frames, interval=10, blit=True, repeat_delay=0)
writer = PillowWriter(fps=23)
ani.save("digits.gif", writer=writer)
