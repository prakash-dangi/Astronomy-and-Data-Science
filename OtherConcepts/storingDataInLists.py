# 1. Using open directly in the for loop, it is not recommended as it does not automatically closes the file, it may create problems.
#   you have to explicitely close the file.
def one():
    data = []
    for line in open("data.csv"):
        data.append(line.strip().split(","))
    
    print(data)

# 2. Using with open(), it is recommended as it closes the file after the operation.

def two():
    with open("data.csv", "r") as csvfile:
        data = [line.strip().split(",") for line in csvfile]

    print(data)

#this data, however, is stored in the list as a string; because the split() method returns string after splitting elements from any type of data

#to store the data as float so that the list is meaningful for mathematical calculations, use this code:

def three():
    data = []
    with open("data.csv", "r") as csvfile:
        for line in csvfile:
            row = []
            for col in line.strip().split(","):
                row.append(float(col))
            data.append(row)

    print(data)

#using numpy, numpy has a simpler asarray function to do this conversion.

import numpy as np

def four(): #using numpy
    data = []

    with open("data.csv", "r") as csvfile:
        for line in csvfile:
            data.append(line.strip().split(","))#this creates a list containing the lists of each line in csvfile as before

    data = np.asarray(data, float) #this updates the data list by chaiging the whole list into the list of float numbers
    print(data)

a = input("Which function do you want to run from (one, two, three, four)? please type the name: ")

if a == "one":
    one()
elif a == "two":
    two()
elif a == "three":
    three()
elif a == "four":
    four()
else:
    print("Please enter a valid choice.")
