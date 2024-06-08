import numpy as np
import matplotlib.pyplot as plt

def one():
    data = np.array([[1, 2, 3],
                    [4, 1, 5],
                    [3, 2, 1]])
    print(data)

    flattened_data = data.ravel()
    print(flattened_data)
    print()
    max_index = np.argmax(data)
    print(max_index)

    position = np.unravel_index(max_index, data.shape)
    print(position)

one()