import numpy as np
from astropy.io import fits
import time
import sys

def median_fits(file):
    start = time.perf_counter()

    #loading the files
    data = []
    for i in file:
        with fits.open(i) as hdulist:
            data.append(hdulist[0].data)

    #stacking the images in a 3d array using the np.dstack() function which stacks images along the 2nd axis
    stack = np.dstack(data)

    #calculating the median of each pixels - along the 2nd axis
    median = np.median(stack, axis=2)

    #calculating the memory of the final stacked median file
    memory = stack.nbytes
    memory /= 1024
    end = time.perf_counter() - start

    return median, end, memory    

result = median_fits(['fitsfiles/image0.fits', 'fitsfiles/image1.fits'])
print(result[0][100,100], result[1], result[2])