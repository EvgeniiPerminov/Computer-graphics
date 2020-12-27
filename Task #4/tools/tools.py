import numpy as np

def interRepr(a, b, u):
  return np.array((1 - u) * a + u * b, dtype=np.int32)

def thirdOrdBez(p, num_steps):
  return np.array([p[0] * (1 - t) ** 3 + 3 * p[1] * (1 - t) ** 2 * t + 3 * p[2] * (1 - t) * t ** 2 + p[3] * t ** 3
                   for t in np.linspace(0, 1, num_steps)], dtype=np.int32)