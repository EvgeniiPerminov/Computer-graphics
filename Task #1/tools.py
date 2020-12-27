import numpy as np
from numpy.linalg import norm

def parse_obj_file(path):
    obj_file = open(path, 'r').read()
    parse_dict = {'v': [], 'f': []}

    for line in obj_file.split('\n'):
        split_line = line.split(' ')

        if split_line[0] in ('v', 'f'):
            parse_dict[line[0]].append(split_line[1:])

    return np.float_(parse_dict['v']), np.int_(parse_dict['f']) - 1


def area(v1, v2, v3):
    return 0.5 * norm(np.cross(v1 - v3, v2 - v3))
