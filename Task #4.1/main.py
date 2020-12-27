from PIL import Image

from classes.clock import Clock
from tools.tools import parse_dict, load_json, get_transitions
import numpy as np


n_digits = 10
n_segment = 4
n_points = 4
n_axles = 2

path_to_file = "G:\PycharmProjects\clock\digits.json"
dict_number = load_json(path_to_file)

digits = parse_dict(dict_number, (n_digits, n_segment, n_points, n_axles))
center = np.int32(digits[0].sum(axis=0).sum(axis=0) / (n_segment * n_points))
digits -= center

tr_steps = 10
third_order_bezier_steps = 100
digits = get_transitions(digits, tr_steps, third_order_bezier_steps)

size_clock = (2000, 600)
color_clock = np.array([0, 0, 0])
digits_color = np.array([255, 255, 255])

clock = Clock(digits, tr_steps, third_order_bezier_steps, n_segment, size_clock, color_clock,  digits_color)
clock.start()

