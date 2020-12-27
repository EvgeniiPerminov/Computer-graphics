import json
import numpy as np


def load_json(path_to_file):
    digits_dict = json.load(open(path_to_file, 'r'))
    return digits_dict


def parse_dict(dictionary, size):
    digits_tensor = np.zeros(size)

    for digit, (_, digit_segments) in enumerate(dictionary.items()):
        for segment, (_, segment_value) in enumerate(digit_segments.items()):
            digits_tensor[digit, segment] = np.array(segment_value)

    return digits_tensor


def get_transitions(digits, tr_steps, third_order_bezier_steps):
    n_digits, n_segments, n_points, n_axles = digits.shape
    tensor = np.zeros((n_digits, tr_steps, n_segments, third_order_bezier_steps, n_axles),
                      dtype=np.int32)

    for tr in range(n_digits):
        for step, u in enumerate(np.linspace(0, 1, tr_steps)):
            for segment in range(n_segments):
                first_seg = digits[tr, segment]
                second_seg = digits[(tr + 1) % n_digits, segment]
                tensor[tr, step, segment] = thirdOrdBez(interRepr(first_seg, second_seg, u), third_order_bezier_steps)

    return tensor


def thirdOrdBez(p, num_steps):
    return np.array([p[0] * (1 - t) ** 3 + 3 * p[1] * (1 - t) ** 2 * t + 3 * p[2] * (1 - t) * t ** 2 + p[3] * t ** 3
                     for t in np.linspace(0, 1, num_steps)], dtype=np.int32)


def interRepr(a, b, u):
    return np.array((1 - u) * a + u * b, dtype=np.int32)


def draw_number(number, n_segments, color, img, steps_third_order_bezier):
    for segment in range(n_segments):
        for point in range(steps_third_order_bezier):
            x = number[segment, point, 0]
            y = number[segment, point, 1]
            img[y - 2: y + 2, x - 2: x + 2] = color
