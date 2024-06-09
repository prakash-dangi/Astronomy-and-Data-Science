import numpy as np
import time

import numpy as np

def median_bins(values, B):
    data_mean = np.mean(values)
    data_std = np.std(values)
    
    # Initialize bins
    below_range_bin = 0
    bin_counts = np.zeros(B)
    bin_interval = 2 * data_std / B
    
    # Distribute values into bins
    for item in values:
        if item < data_mean - data_std:
            below_range_bin += 1
        elif item < data_mean + data_std:
            bin_index = int((item - (data_mean - data_std)) / bin_interval)
            bin_counts[bin_index] += 1
        # Values above data_mean + data_std are ignored

    return data_mean, data_std, below_range_bin, bin_counts

def median_approx(values, B):
    # Calculate the mean, standard deviation, and bins for the input data
    data_mean, data_std, below_range_bin, bin_counts = median_bins(values, B)
    
    # Determine the position of the median element
    total_elements = len(values)
    midpoint = (total_elements + 1) / 2

    cumulative_count = below_range_bin
    for bin_index, count in enumerate(bin_counts):
        cumulative_count += count
        if cumulative_count>= midpoint:
            # Stop when the cumulative count surpasses the midpoint
            break

    bin_interval = 2 * data_std / B
    median_estimate = data_mean - data_std + bin_interval * (bin_index + 0.5)
    return median_estimate


# def median_bins(values, B):
#     data = values
#     mu = np.mean(data)
#     sig = np.std(data)

#     minval = mu - sig
#     maxval = mu + sig

#     sorted = [x for x in data if minval <=x <= maxval]

#     bin_width = 2*sig/B

#     bins = [[None]*3 for i in range(B+1)]
#     ignoreBinLength = len([x for x in data if x < minval])
#     print(ignoreBinLength )
#     bins[0][2] = ignoreBinLength

#     #assigning ranges to bins and initialising the counts
#     mi = minval
#     # start = time.perf_counter()
#     for i in range(1,B+1):
#         ma = mi + bin_width
#         bins[i][0] = mi 
#         bins[i][1] = ma 
#         bins[i][2] = len([x for x in sorted if mi <= x < ma])
#         # bins[i][2] = len([x for x in data if mi <= x < ma]) #for time difference calculation
#         mi = ma
#     # end = time.perf_counter() - start
#     # print(end)

#     print(bins)

#     # one more way to write the below code
#     # binCounts = np.empty(len(bins))
#     # for i in range(len(bins)):
#     #     binCounts[i] = bins[i][2]

#     binCounts = np.array([])
#     for i in range(1, B+1):
#         binCounts = np.append(binCounts, bins[i][2])

#         print(binCounts)

#     return mu, sig, bins[0][2], binCounts

# print(median_bins([1, 1, 3, 2, 2, 6], 4))

# def median_approx(values, B):
#     t = median_bins(values, B)
#     mu = t[0]
#     sig =t[1]

#     data = values
#     N = np.size(data)
#     if N%2 == 0:
#         median_pos = (N/2 + (N/2 + 1))/2
#     else:
#         median_pos = (N+1)/2

#     count = t[2]
#     iteration = 0
#     for i in t[3]:
#         count += i
#         iteration += 1
#         if count >= median_pos:
#             medBin = iteration #the bin which contains median, its not the index of median containing bin, its the bin number itself.
#             break
#         else:
#             continue
    
#     #get the range of the bin which contains the median
#     minimum = (mu - sig) + (medBin - 1)*2*sig/B 
#     maximum = (mu - sig) + (medBin)*2*sig/B
#     median = (minimum + maximum)/2
#     return median

# print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
# print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
# print(median_approx([1,1,3,2,2,6], 3))
# print(median_bins([1,1,3,2,2,6], 3))

print(median_bins([1, 1, 3, 2, 2, 6], 3))
print(median_approx([1, 1, 3, 2, 2, 6], 3))
print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))

# solution code
# import numpy as np

# def median_bins(values, B):
#   mean = np.mean(values)
#   std = np.std(values)
    
#   # Initialise bins
#   left_bin = 0
#   bins = np.zeros(B)
#   bin_width = 2*std/B
    
#   # Bin values
#   for value in values:
#     if value < mean - std:
#       left_bin += 1
#     elif value < mean + std:
#       bin = int((value - (mean - std))/bin_width)
#       bins[bin] += 1
#     # Ignore values above mean + std

#   return mean, std, left_bin, bins


# def median_approx(values, B):
#   # Call median_bins to calculate the mean, std,
#   # and bins for the input values
#   mean, std, left_bin, bins = median_bins(values, B)
    	
#   # Position of the middle element
#   N = len(values)
#   mid = (N + 1)/2

#   count = left_bin
#   for b, bincount in enumerate(bins):
#     count += bincount
#     if count >= mid:
#       # Stop when the cumulative count exceeds the midpoint
#       break

#   width = 2*std/B
#   median = mean - std + width*(b + 0.5)
#   return median