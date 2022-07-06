import numpy as np

def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
      
    y = np.array(list).reshape(3,3)

    mean1 = np.mean(y,axis=0).tolist()
    mean2 = np.mean(y,axis=1).tolist()
    mean3 = np.mean(y).tolist()

    var1 = np.var(y,axis=0).tolist()
    var2 = np.var(y,axis=1).tolist()
    var3 = np.var(y).tolist()

    std1 = np.std(y,axis=0).tolist()
    std2 = np.std(y,axis=1).tolist()
    std3 = np.std(y).tolist()

    max1 = np.max(y,axis=0).tolist()
    max2 = np.max(y,axis=1).tolist()
    max3 = np.max(y).tolist()

    min1 = np.min(y,axis=0).tolist()
    min2 = np.min(y,axis=1).tolist()
    min3 = np.min(y).tolist()

    sum1 = np.sum(y,axis=0).tolist()
    sum2 = np.sum(y,axis=1).tolist()
    sum3 = np.sum(y).tolist()

    calculations = {
    'mean': [mean1, mean2, mean3],
    'variance': [var1, var2, var3],
    'standard deviation': [std1, std2, std3],
    'max': [max1, max2, max3],
    'min': [min1, min2, min3],
    'sum': [sum1, sum2, sum3]
    }
      
    return calculations
    
    
    