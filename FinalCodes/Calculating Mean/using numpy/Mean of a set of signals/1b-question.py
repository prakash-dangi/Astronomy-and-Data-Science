# Mean of a set of signals
import numpy as np
def mean_datasets(x): #where x is a list of files as an input
    dataset = np.array(x) #aactually there is no meaning of making this a numpy array as x has string elements.
    arrayList = []
    for set in dataset:
        with open(f"{set}", "r") as csvfile:
            arrayList.append(np.loadtxt(csvfile, delimiter=","))

    a = sum(arrayList)
    if len(dataset) == 0:
        print("No data present in the given dataset")
    else:
        meanArray = np.round(a/len(dataset), 1)

    return meanArray

filePaths = ["Calculating Mean\\using numpy\\Mean of a set of signals\\data1.csv", 
             "Calculating Mean\\using numpy\\Mean of a set of signals\\data2.csv", 
             "Calculating Mean\\using numpy\\Mean of a set of signals\\data3.csv"]

print(mean_datasets(filePaths))


#the more efficient code for this example could be: 
'''import numpy as np

def mean_datasets(filenames):
  n = len(filenames)
  if n > 0:
    data = np.loadtxt(filenames[0], delimiter=',')
    for i in range(1,n):
      data += np.loadtxt(filenames[i], delimiter=',')
    
    # Mean across all files:
    data_mean = data/n
     
    return np.round(data_mean, 1)'''
