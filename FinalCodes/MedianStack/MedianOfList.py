import time
def median_odd(inputList):
    inputList.sort() #the sort() method does not return a list, instead it just modifies a list.
    mid = len(inputList)//2
    median = inputList[mid]
    return median

def median_even(inputList):
    inputList.sort()
    mid = len(inputList)//2
    # print(sortedList)
    median = (inputList[mid-1] + inputList[mid])/2
    return median

def mean_list(inputList):
    mean = sum(inputList)/len(inputList)
    return mean

def list_stats(inputList):
    if len(inputList)%2 == 0:
        median = median_even(inputList)
        mean = mean_list(inputList)
        return median, mean
        
    elif len(inputList)%2 != 0 and len(inputList) > 1:
        median = median_odd(inputList)
        mean = mean_list(inputList)
        return median, mean

    else:
        median = inputList[0]
        mean = inputList[0]
        return median, mean

start = time.perf_counter_ns()     
a = list_stats([1.3, 2.4, 20.6, 0.95, 3.1])
print(a)
end = time.perf_counter_ns() - start
print(end)