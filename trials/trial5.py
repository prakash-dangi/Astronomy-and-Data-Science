# to understand the difference between numpy's np.sum() function and built-in sum() function.

import numpy as np

array1 = []
print(type(array1))
for a in range(1, 5):
    array1.append(a)

print(type(array1))

a = sum(array1)
print(type(array1))


data = np.array([1, 2, 3, 4, 5, 7])
data2 = np.array([1, 2, 3, 4, 5, 6])
e = [data, data2]
f = np.array([data, data2])
print()
print(type(e))
print()
print(type(f))
print()
g = sum(e)
print(type(g))
print(g)
h = np.sum(e)
print(type(h))
print(h)
print()
i = sum(f)
print(type(f))
print(f)
print()
j = np.sum(f)
print(type(j))
print(j)


b = sum(data)
print(type(data))
c = np.sum(data)
print(type(c))
print(c)

# try:
#   result = sum(data)
#   print(result)
# except TypeError as e:
#   print("Built-in sum() doesn't work with NumPy arrays. Use np.sum instead.")
