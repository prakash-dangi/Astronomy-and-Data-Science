import numpy as np
import time
import statistics

def time_stat(func, size, ntrials):
  trialSum = 0
  for i in range(0, ntrials):
    data = np.random.rand(size)
    start = time.perf_counter()
    res = func(data)
    end = time.perf_counter() - start
    trialSum += end


  avgTime = trialSum/ntrials
  return avgTime
  
if __name__ == "__main__":
    print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
    print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))