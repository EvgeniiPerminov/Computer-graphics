import numpy as np


def rotation_mx(ang):
    mtr = np.array([[np.cos(ang), -np.sin(ang), 0],
                    [np.sin(ang), np.cos(ang), 0],
                    [0, 0, 1]])
    return mtr


def shift_mx(vec):
    mtr = np.array([[1, 0, vec[0]],
                    [0, 1, vec[1]],
                    [0, 0, 1]])
    return mtr


def to_proj_coords(x):
    r, c = x.shape
    x = np.concatenate([x, np.ones((1, c))], axis=0)
    return x


def diag_mx(k):
    mtr = np.array([[k, 0, 0],
                    [0, k, 0],
                    [0, 0, 1]])
    return mtr


def to_cart_coords(x):
    x = x[:-1] / x[-1]
    return x
