from tools import parse_obj_file, area
import numpy as np

obj_path = 'source/teapot.obj'
vertexes, faces = parse_obj_file(obj_path)

num_vertexes = vertexes.shape[0]
num_faces = faces.shape[0]

min_x, min_y, min_z = np.min(vertexes, axis=0)
max_x, max_y, max_z = np.max(vertexes, axis=0)

# Area of all faces
faces_area = 0
for v1, v2, v3 in faces:
    faces_area += area(vertexes[v1], vertexes[v2], vertexes[v3])


print(f"Vertexes: {num_vertexes}, faces: {num_faces}\n"
      f"MIN x:{min_x}, y:{min_y}, z:{min_z}\n"
      f"MAX x:{max_x}, y:{max_y}, z:{max_z}\n"
      f"Area: {np.round(faces_area, 1)}")
