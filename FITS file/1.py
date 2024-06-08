#accessing data from a fits file
def one():
    from astropy.io import fits

    hdulist = fits.open("fitsfiles\image0.fits")
    hdulist.info()

one()