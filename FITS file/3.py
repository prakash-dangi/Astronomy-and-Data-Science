# Plotting image from the FITS file using Matplotlib

from astropy.io import fits
import matplotlib.pyplot as plt

def one():
    hudlist = fits.open("fitsfiles\image0.fits")
    data = hudlist[0].data

    #plotting the 2d array stored in the data variable

    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel("X-pixels (RA)") # RA = Right Acession - celestial coordinate system - longitude - hrs, min, sec
    plt.ylabel("Y-pixels (Dec)") #Dec = Declination - celestial coordinate system - angular - latitude - hrs, min, sec
    plt.colorbar()
    plt.show()

one()