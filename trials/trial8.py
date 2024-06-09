#to understand the operations on numpy arrays
import numpy as np

def one():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(a + 3)
    print(a*3)
    b = np.array([[1, 2], [1, 2], [1, 2]])
    # print(a + b)
    print()
    # print(a*b)
    print(np.matmul(a, b))
    c = 2*a/3
    print(c)
    a[0][0] = b[1][1]
    print(a)
    return


def two():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    for point in a:
        print(point)
        
    return

one()