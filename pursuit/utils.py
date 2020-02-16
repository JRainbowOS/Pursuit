import numpy as np 

def make_unit_vector(dx, dy):
    norm = np.sqrt(dx ** 2 + dy ** 2)
    return dx / norm, dy / norm