import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

def one():
    hdulist = fits.open('fitsfiles/image0.fits')
    data = hdulist[0].data
    
    hdulist = fits.open('fitsfiles/image1.fits')
    data2 = hdulist[0].data

    c = np.array([data, data2])
    d = sum(c)

    print(type(d))
    print()
    print()
    print(d)
    print("1")

    print(data2)
    print("1")
    print(data)
    print("1")

    a = data + data2
    print(type(a))
    print("1")
    print(a)
    
    b = a/2

    print("1")
    print(type(b))
    print(b)

one()