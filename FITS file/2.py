#Reading FITS files

from astropy.io import fits

def one():
    for file in range(0,12):
        hdulist = fits.open(f"fitsfiles/image{file}.fits")
        a = hdulist[0].data
        print(a.shape)

one()   