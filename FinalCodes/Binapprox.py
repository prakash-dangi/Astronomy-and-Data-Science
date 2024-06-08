import numpy as np
import time

def median_bins(values, B):
    data = values
    mu = np.mean(data)
    sig = np.std(data)

    minval = mu - sig
    maxval = mu + sig

    sorted = [x for x in data if minval <=x <= maxval]

    bin_width = 2*sig/B

    bins = [[None]*3 for i in range(B+1)]
    ignorebin = len([x for x in data if x < minval])
    bins[0][2] = ignorebin

    #assigning ranges to bins and initialising the counts
    mi = minval
    # start = time.perf_counter()
    for i in range(1,B+1):
        ma = mi + bin_width
        bins[i][0] = mi 
        bins[i][1] = ma 
        bins[i][2] = len([x for x in sorted if mi <= x < ma])
        # bins[i][2] = len([x for x in data if mi <= x < ma]) for time difference calculation
        mi = ma
    # end = time.perf_counter() - start
    # print(end)

    # print(bins)

    # one more way to write the below code
    # binCounts = np.empty(len(bins))
    # for i in range(len(bins)):
    #     binCounts[i] = bins[i][2]

    binCounts = np.array([])
    for i in bins:
        binCounts = np.append(binCounts, i[2])

    print(binCounts)

    return mu, sig, bins[0][2], binCounts

# print(median_bins([1, 1, 3, 2, 2, 6], 4))

def median_approx(values, B):
    t = median_bins(values, B)
    mu = t[0]
    sig =t[1]

    data = values
    N = np.size(data)
    if N%2 == 0:
        median_pos = (N/2 + (N/2 + 1))/2
    else:
        median_pos = (N+1)/2

    count = 0
    iteration = 0
    for i in t[3]:
        count += i
        iteration += 1
        if count >= median_pos:
            medBin = iteration #the bin which contains median, its not the index of median containing bin, its the bin number itself.
            break
        else:
            continue
    
    #get the range of the bin which contains the median
    min = (mu - sig) + (medBin - 1)*2*sig/B
    max = (mu - sig) + (medBin)*2*sig/B
    median = (min + max)/2
    return median

print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))