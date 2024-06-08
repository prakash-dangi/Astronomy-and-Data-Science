#The NumPy loadtxt function can automatically read a CSV file into a NumPy array, including converting from string to numbers.

import numpy as np

data = np.loadtxt("data.csv", delimiter=",")
print(data)