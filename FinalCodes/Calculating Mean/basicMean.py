def calculate_mean(indata):
    if not isinstance(indata, list):
        raise TypeError("Input data must be a list of numbers")
    
    data_sum = sum(indata)

    if len(indata) == 0:
        return None
    
    mean = data_sum/len(indata)

    return mean

if __name__ == "__main__":
    mean = calculate_mean([1,2.2,0.3,3.4,7.9])
    print(mean)