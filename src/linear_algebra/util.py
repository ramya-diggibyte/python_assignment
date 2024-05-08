import numpy as np

def linear_algebra(input_array):
    a = np.array(input_array)
    determinant = np.linalg.det(a)
    return round(determinant, 1)