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
                    if data[i, j] < mi[i, j]:
                        ignore_bins[i, j] += 1
                    elif data[i, j] < ma[i, j]:
                        bin_index = int((data[i, j] - (mi[i, j]))/bin_width[i, j])
                        bins[i, j, bin_index] += 1
        
                
    return mu, sig, ignore_bins, bins

def median_approx_fits(filenames, B):
    mu, sig, ignore_bins, bins = median_bins_fits(filenames, B)
    mi = np.array(mu - sig)
    ma = np.array(mu + sig)
    dim = mu.shape

    bin_width = 2*sig/B

    # if len(filenames)%2 == 0:
    #     median_pos = (len(filenames) + (len(filenames)/2 + 1))/2
    # else:
    #     median_pos = (len(filenames)+1)/2
    N = len(filenames)
    median_pos = (N + 1)/2

    bins_count = ignore_bins
    median = np.zeros(dim)

    #-------------------------------------------------------------------------
    #this is the code which i learned from grock solution, it is used to update the best solution which is marked by ** below
    # for i in range(dim[0]):
    #     for j in range(dim[1]):
    #         count = ignore_bins[i, j]
    #         for index, bincount in enumerate(bins[i, j]):
    #             count  += bincount
    #             if count >= median_pos:
    #                 break
    #         median[i, j] = mi[i, j] + bin_width[i, j]*(index + 0.5)
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    #THIS IS THE PART WHICH WAS HAVING PROBLEMS- WRONG CODE LOGIC-
    # #counting and finding the bin containing the median 
    # median_bin = np.zeros(dim)
    # for index, count in np.ndenumerate(bins):
    #     bins_count[index[0], index[1]] += count
    #     if bins_count[index[0], index[1]] >= median_pos:
    #         median_bin[index[0], index[1]] = index[2]
    #-------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------
    # #this is the correction done to the previous WRONG LOGIC CODE, but much better solution is next to this one        
    # y = 0
    # u = None
    # median_bin = np.zeros(dim)
    # for index, count in np.ndenumerate(bins):
    #     if u != index[1] or u == None:
    #         y = 0
    #     else:
    #         y = 1
    #     bins_count[index[0], index[1]] += count
    #     if bins_count[index[0], index[1]] >= median_pos:
    #         if y == 0:
    #             median_bin[index[0], index[1]] = index[2]
    #             y += 1
    #             u = index[1]
    #         else:
    #             continue
    #-------------------------------------------------------------------------

    #(**)---------------------------------------------------------------------
    #(**)correct approach for counting and finding the bin containing the median(**)
    median_bin = np.zeros(dim)
    for i in range(dim[0]):
        for j in range(dim[1]):
            for index, count in enumerate(bins[i, j]):
                bins_count[i, j] += count
                if bins_count[i, j] >= median_pos:
                    break
            median_bin[i, j] = index
    #-------------------------------------------------------------------------
    
    #median calculation
    for i in range(dim[0]):
        for j in range(dim[1]):
            median[i, j] = mi[i, j] + bin_width[i, j]*(median_bin[i, j] + 0.5)
    
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
median_bins_fits(['fitsfiles/image0.fits', 'fitsfiles/image1.fits', 'fitsfiles/image2.fits'], 5)