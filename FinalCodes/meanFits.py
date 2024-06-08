import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

def mean_fits(files):
    # FileData = filename
    # data = np.array([])
    print(files)

    with fits.open(files[0]) as hdulist:
        data = hdulist[0].data

    for i in range(1, len(files)):
        with fits.open(files[i]) as hdulist:
            data += hdulist[0].data

    # sumData = sum(data)
    # print()
    # print(sumData)

    if len(files) == 0:
        print("There is no data entered.")
        return
    
    meanData = data/len(files)
    print()
    print(meanData)


    return meanData

# from astropy.io import fits
# import numpy as np

# def mean_fits(files):
#   n = len(files)
#   if n > 0:
    
#     hdulist = fits.open(files[0])
#     data = hdulist[0].data
#     hdulist.close()
    
#     for i in range(1, n):
#       hdulist = fits.open(files[i])
#       data += hdulist[0].data
#       hdulist.close()
    
#     mean = data / n
#     return mean

# a = ['fitsfiles/image0.fits', 'fitsfiles/image1.fits', 'fitsfiles/image2.fits', 'fitsfiles/image3.fits', 'fitsfiles/image4.fits', 'fitsfiles/image5.fits', 'fitsfiles/image6.fits', 'fitsfiles/image7.fits', 'fitsfiles/image8.fits', 'fitsfiles/image9.fits', 'fitsfiles/image10.fits', 'fitsfiles/image11.fits']
a = ['fitsfiles/image0.fits', 'fitsfiles/image1.fits', 'fitsfiles/image2.fits']
b = mean_fits(a)
print(b)
print()
print(b[100,100])

