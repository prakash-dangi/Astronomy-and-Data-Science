import numpy as np

data = np.array([ [3, 5, 1], 
                  [7, 2, 9] ])

# Find the index of the maximum value in the entire flattened array
max_index = np.argmax(data)  # max_index will be 5 (index of 9)

# Find the index of the maximum value along each column (axis=0)
col_wise_max_indices = np.argmax(data, axis=0)  # col_wise_max_indices will be [1, 0, 1]

# Find the index of the maximum value along each row (axis=1)
row_wise_max_indices = np.argmax(data, axis=1)  # row_wise_max_indices will be [1, 1]

print(max_index)
print()
print(row_wise_max_indices)
print()
print(col_wise_max_indices)

print(data[1,2])