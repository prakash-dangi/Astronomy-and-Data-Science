import numpy as np
def calc_stats(x):
    data = np.loadtxt(f"{x}", delimiter=",")

    meanData = np.round(np.mean(data), 1)
    medianData = np.round(np.median(data), 1)
    print(str(meanData) + " " + str(medianData))

    statTuple = (meanData, medianData)

    print(statTuple)

    return meanData, medianData

x = "data.csv"

stats = calc_stats(x)

print(stats)