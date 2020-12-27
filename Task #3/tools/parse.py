import numpy as np


def parse_obj_file(path):
    obj_file = open(path, 'r').read()
    parse_dict = {'v': [], 'f': []}

    for line in obj_file.split('\n'):
        split_line = line.split(' ')

        if split_line[0] in ('v', 'f'):
            parse_dict[line[0]].append(split_line[1:])

    return np.float_(parse_dict['v']), np.int_(parse_dict['f']) - 1
