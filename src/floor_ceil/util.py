import numpy as np
def floor_ceil_rint(input_array):
    np.set_printoptions(legacy='1.13')  # Setting legacy for printing purpose.
    floor_f = np.floor(input_array)
    ceil_c = np.ceil(input_array)
    rint_r = np.rint(input_array)
    return f"{floor_f}\n{ceil_c}\n{rint_r}"