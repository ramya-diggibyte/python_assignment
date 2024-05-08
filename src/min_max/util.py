import numpy as np

def max_of_min_in_rows():
    N, M = map(int, input("Enter the dimensions of the array (N M): ").split())

    # Take input for the array elements
    print("Enter the elements of the array:")
    array_input = []
    for i in range(N):
        row_input = list(map(int, input().split()))
        array_input.append(row_input)

    # Convert the input into a NumPy array
    a = np.array(array_input)
    max_of_min = np.max(np.min(a, axis=1))
    return max_of_min