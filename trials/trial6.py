import numpy as np
# from astropy.io import fits
# import time
# import sys

# def median_fits(file):
#     N = len(file)
#     if N == 0:
#         return
    
#     data = np.array([])
#     for i in file:
#         with fits.open(i) as hdulist:
#             data = (hdulist[0].data)

#     m = np.median(data)

#     print(m)

a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])
b = np.array([[2, 3, 4], 
              [5, 6, 7], 
              [8, 9, 10]])
c = np.array([[3, 4, 5], 
              [6, 7, 8], 
              [9, 10, 11]])
d = np.array([a, b, c])
# print(d)
# print(np.median(d))

# e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# f = np.median(e)
# print(f)
# e.sort()
# print(e)

# for i in d:
#     print(i) #access the  i'th array in d
#     for j in i:
#         print(j) #access the j'th row in i, i.e. the j'th list in that array
#         for k in j:
#             print(k) #access the k'th element in the j'th row of the i'th array

#this block of code make a list "inter" which contains the list of elements corresponding to the same coordinates in the collection of arrays "d"
inter = []
inter3 = []
inter2 = []
# for i in range(9):
# for row in range(3): #loop for changing the row in each element in every array of d
#     for column in range(3): #loop for changing the element of every array in d
#         for array in range(len(d)): #loop for changing the element arrays in d
#             # print(d[array, row, column])
#             inter2.append(d[array, row, column]) #selects the [array, row, column] element and appends to inter2
                
#         inter3.append(inter2)
#         inter2 = []

#     inter.append(inter3)
#     inter3 = []

# print(inter)
# print(np.array(inter))
# print(np.array(inter).shape)

for row in range(3):
    inter3 = []
    for column in range(3):
        inter2 = []
        for array in range(len(d)):
            inter2.append(d[array, row, column])

        inter3.append(inter2)
    inter.append(inter3)

print(inter)
print(np.array(inter))
print(np.array(inter).shape)

median_array = []
for i in inter:
    median_arrayList = []
    if len(i)%2 == 0:
        m = len(i)//2
        median = (i[m-1] + i[m])/2
        median_arrayList.append(median)
        median_array.append(median_arrayList)

    else:
        print(i)
        print(len(i))
        m = len(i)//2
        median = i[m]
        print(i[m])
        median_arrayList.append(median)
        median_array.append(median_arrayList)
        
print(median_array)
t = np.array(median_array)
print(t)
print(t[1,0,1])