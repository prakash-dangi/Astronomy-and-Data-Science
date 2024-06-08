#without using numpy
# Define a 3x3 matrix 
def one():
    # Define a 3x3 matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Accessing elements by row and column index
    element11 = matrix[0][0]  # element at row 1 (index 0), column 1 (index 0) - value: 1
    element23 = matrix[1][2]  # element at row 2 (index 1), column 3 (index 2) - value: 6

    # Printing the matrix (optional)
    for row in matrix:
        print(row)

def two():
    matrix = [
        [1, 2, [[1,2,3],
                [11,22,33],
                [44,55,66]]],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Accessing elements by row and column index
    element11 = matrix[0][0]  # element at row 1 (index 0), column 1 (index 0) - value: 1
    element23 = matrix[1][2]  # element at row 2 (index 1), column 3 (index 2) - value: 6
    element1312 = matrix[0][2][2][1]
    # Printing the matrix (optional)
    for row in matrix:
        print(row)

    print(element11)
    print(element1312)

#with numpy

def three():
    import numpy as np

    # Define a 3x3 matrix using NumPy
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],  
        [7, 8, 9]
    ])

    # Accessing elements (similar to nested lists)
    element11 = matrix[0, 0]   # element at row 1 (index 0), column 1 (index 0) - value: 1
    element23 = matrix[1, 2]   # element at row 2 (index 1), column 3 (index 2) - value: 6

    # Printing the matrix (using NumPy's print function)
    print(matrix)

a = input("Which function do you want to run from (one, two, three, four)? please type the name: ")

if a == "one":
    one()
elif a == "two":
    two()
elif a == "three":
    three()
else:
    print("Please enter a valid choice.")