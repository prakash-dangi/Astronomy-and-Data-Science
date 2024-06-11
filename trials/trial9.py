import numpy as np

a = np.array([[5, 7, 7], 
              [6, 3, 10], 
              [10, 3, 4]])

b = np.array([[2, 7, 4], 
              [10, 9, 6], 
              [6, 5, 1]])

c = np.array([[6, 9, 6], 
              [3, 5, 2], 
              [1, 1, 3]])

d = np.array([[7, 2, 9], 
              [1, 6, 4], 
              [10, 5, 3]])

e = np.array([[4, 10, 6], 
              [8, 2, 7], 
              [3, 9, 1]])

f = np.array([[5, 1, 3], 
              [7, 4, 8], 
              [2, 6, 9]])

g = np.array([[6, 3, 5], 
              [9, 10, 1], 
              [4, 2, 8]])

h = np.array([[2, 7, 4], 
              [5, 3, 6], 
              [8, 1, 10]])

k = np.array([[9, 6, 2], 
              [1, 5, 10], 
              [3, 4, 7]])

l = np.array([[10, 8, 1], 
              [7, 4, 9], 
              [6, 5, 3]])

m = np.array([[1, 5, 7], 
              [3, 8, 2], 
              [9, 6, 4]])
 
n = np.array([[8, 3, 6], 
              [4, 10, 5], 
              [2, 9, 7]])

o = np.array([[3, 7, 8], 
              [6, 2, 4], 
              [1, 10, 5]])

data = [a, b, c, d, e, f, g, h, k, l, m, n, o]

def stats(data):
    d = np.array(data)
    mean = np.mean(d, axis=0)
    std = np.std(d, axis=0)
    return mean, std

def median_bins(data, B):
    mu, sig = stats(data)
    # print(sig)
    dim = mu.shape

    mi = mu-sig
    ma = mu+sig
    bin_width = 2*sig/B
    # print(bin_width)

    #assign values to bins
    ignoreBin = np.zeros(dim)
    bins = np.zeros((dim[0], dim[1], B))

    for array in data:
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i, j] < mi[i, j]:
                    ignoreBin[i, j] += 1
                elif array[i, j] > mi[i, j] and array[i, j] < ma[i, j]:
                    binIndex = int((array[i, j] - mi[i, j])/bin_width[i, j])
                    bins[i, j, binIndex] += 1 #here i denotes the row of each input array which corresponds to the entire array element in bin, j denotes the column of each input array which corresponds to the row of that array in bin which is denoted by i and binIndex denotes the bin number which corresponds to the column number of the array in bin which is denoted by i.
                    '''here, each plane(or array) = i in bin denotes the row of the input array
                    and in the plane, each row(=j) denotes the column of the input array. Therefore
                    by giving (i, j) in bins, we talk about each data point in the input array.
                    As there are multiple input arrays of similar shape, and each data point index 
                    have multiple values (= number of input arrays), and every index has B bins, to
                    denote the bins we use the column of the array given by i in bins as the bin column.
                    therefore, the array denotes the row of input array, row of that array in bins denote
                    the column and column of that array in bins denote the bin set of B bins for each datapoint
                    index in input arrays.'''
    return mu, sig, ignoreBin, bins

def median_approx(data, B):
    mu, sig, ignoreBin, bins = median_bins(data, B)
    mi = np.array(mu - sig)
    ma = np.array(mu + sig)
    dim = mu.shape
    # print(dim)
    bin_width = 2*sig/B
    median_pos = (len(data)+1)/2

    countBin = ignoreBin
    bin_index = np.zeros(dim)

    for index, count in np.ndenumerate(bins):
        print(index)
        countBin[index[0], index[1]] += count
        if countBin[index[0], index[1]] >= median_pos:
            bin_index[index[0], index[1]] = index[2]

    median = np.zeros(dim)
    for i in range(dim[0]):
        for j in range(dim[1]):
            median[i, j] = mi[i, j] + bin_width[i, j]*(bin_index[i, j] + 0.5)
    
    return median

median_bins(data, 5)
median_approx(data, 5)
print(median_approx(data, 5))



# for t in data:
#         for i in range(dim[0]):
#             for j in range(dim[1]):
#                 value = t[i, j]
#                 # print(value)

#                 if value < mi[i, j]:
#                     ignoreBin[i, j] += 1
                        
#                 elif value >= mi[i, j] and value < ma[i, j]:
#                     bin = int((value - (mi[i, j]))/bin_width[i, j])
#                     bins[i, j, bin] += 1