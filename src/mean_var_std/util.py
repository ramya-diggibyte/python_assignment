import numpy as np

def mean_var_std(input_array):
    mean_cal = np.mean(input_array, axis=1)
    var_cal = np.var(input_array, axis=0)
    std_cal = round(np.std(input_array, axis=None), 11)
    mean_var_std_result = f"{mean_cal}\n{var_cal}\n{std_cal}"
    return mean_var_std_result