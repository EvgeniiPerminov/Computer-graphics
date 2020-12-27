import numpy as np
import json


def parse_json_file(path, json_info):
    dictionary = json.load(open(path, 'r'))
    digits_tensor = np.zeros(json_info, dtype=np.int32)

    for digit, (_, digit_segments) in enumerate(dictionary.items()):
        for segment, (_, segment_value) in enumerate(digit_segments.items()):
            digits_tensor[digit, segment] = np.array(segment_value)

    return digits_tensor
