from math import copysign


def bresenham(img, color, x0, y0, x1, y1):
    mx, dx = int(copysign(1, x1 - x0)), abs(x1 - x0)
    my, dy = int(copysign(1, y1 - y0)), abs(y1 - y0)
    sx, sy, s, l = (mx, 0, dy, dx) if dx > dy else (0, my, dx, dy)
    x, y, error = x0, y0, 0

    for _ in range(l):
        error -= s
        if error < 0: error, x, y = error + l, x + mx, y + my
        else: x, y = x + sx, y + sy
        img[y, x] = color