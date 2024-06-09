from helper import running_stats
from astropy.io import fits
import numpy as np

def median_bins_fits(filenames, B):
    mu, sig = running_stats(filenames)

    mi = np.array(mu - sig)
    ma = np.array(mu + sig)
    bin_width = 2*sig/B

    #initialize bins
    ignore_bins = np.zeros_like(mu)
    bins = np.empty([200, 200, B])

    #take values in bins
    for filename in filenames:
        with fits.open(filename) as hdulist:
            data = hdulist[0].data
            for i in range(len(data)): #accessing the rows in the data array
                for j in range(len(data[i])): #accessing the columns in the data, to finaly access each point as it is a 2D array
                    if data[i][j] < mi[i][j]:
                        ignore_bins[i][j] += 1
                    elif data[i][j] < ma[i][j]:
                        bin_index = int((data[i][j] - (mi[i][j]))/bin_width[i][j])
                        bins[i][j][bin_index] += 1
        
                
    return mu, sig, ignore_bins, bins

def median_approx_fits(filenames, B):
    mu, sig, ignore_bins, bins = median_bins_fits(filenames, B)

    bin_width = 2*sig/B

    if len(filenames)%2 == 0:
        median_pos = (len(filenames) + (len(filenames)/2 + 1))/2
    else:
        median_pos = (len(filenames)+1)/2

    bins_count = ignore_bins
    median = np.zeros_like(bins_count)

    #counting and finding the bin containing the median 
    median_bin = np.zeros_like(median)
    for i in range(len(mu)):
        for j in range(len(mu[i])):
            for index, count in np.ndenumerate(bins[i][j]):
                bins_count[i][j] += count
                if bins_count[i][j] >= median_pos:
                    median_bin[i][j] = index[0]

    #median calculation
    for i in range(len(median_bin)):
        for j in range(len(median_bin[i])):
            median[i][j] = mu[i][j] - sig[i][j] + bin_width[i][j]*(median_bin[i][j] + 0.5)
    
    return median

mean, std, left_bin, bins = median_bins_fits(['fitsfiles/image0.fits', 'fitsfiles/image1.fits', 'fitsfiles/image2.fits'], 5)
median = median_approx_fits(['fitsfiles/image0.fits', 'fitsfiles/image1.fits', 'fitsfiles/image2.fits'], 5)

print(mean[100,100])
print(std[100,100])
print(left_bin[100,100])
# print(np.shape(bins))
print(bins[100,100, :])
# print(bins)
print(median[100, 100])
# median_bins_fits(['fitsfiles/image0.fits', 'fitsfiles/image1.fits', 'fitsfiles/image2.fits'], 5)