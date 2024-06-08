import numpy as np

fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
m = np.mean(fluxes)
print(m)

#by converting the float number into a string inside the print function.
print("the length of the given array is " + str(np.size(fluxes))) 
print("the standard deviation of this data set is " + str(np.std(fluxes)))
#using format string method.
print(f"the length of the given array is {np.size(fluxes)}.")
print(f"the standard deviation of this data set is {np.std(fluxes)}.")


