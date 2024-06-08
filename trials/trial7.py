import numpy as np

L = [[None]*3 for i in range(3)]
print(L)
print(len(L[0]))
ignore = 2
L[0][0] = ignore
L[1][0] = 1
L[1][1] = 2
L[1][2] = 3
print(L)
data = [1, 1, 3, 2, 2, 6]
minval = 6
ignore = len([x for x in data if x < minval])
t = 0
for x in data:
    if t == 1:
        x = data[0]
    if x < minval:
        data.remove(x)
        t = 1
    else:
        t = 0

print(data)
# print([x for x in data if x < minval])
print(ignore)