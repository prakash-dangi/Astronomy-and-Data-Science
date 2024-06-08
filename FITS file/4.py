# Write a load_fits function that loads in a FITS file and finds the position of the brightest pixel (i.e. the maximum value) in its image data. To make this function work for arbitrary files, pass the name of the FITS file as an argument to the function.
import matplotlib.pyplot as plt
from astropy.io import fits 
import numpy as np

def load_fits():
    with fits.open(r"fitsfiles\image2.fits") as hdulist:
        data = hdulist[0].data

    # max_index_x = np.argmax(data)
    # max_index_y = np.argmax(data, axis=1)

    # print(max_index_x)
    # print()
    # print(max_index_y)
    # print()

    # max_index = tuple((np.argmax(data, axis=0), np.argmax(data, axis=1)))
    max_index = np.argmax(data)
    print(max_index)

    max_pos = np.unravel_index(max_index, data.shape) #here we use the unravel_index function as the argmax index flattens the original array internally (ravells it), to unravell it or to make it an array again, use the unravel_index function, with the shape of data
    print(max_pos)

    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.xlabel("X-pixels (RA)")
    plt.ylabel("Y-pixels (Dec)")
    plt.colorbar()
    plt.show()

    # return max_index

load_fits()