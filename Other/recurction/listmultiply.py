import numpy as np


a = []
b = []
def inputData(a):
    for i in range(3):
        sublist = input("Enter sublist {} (comma-separated values): ".format(i+1)).split(',')
        sublist = [int(x) for x in sublist]
        a.append(sublist)
        return a



res = np.multiply(inputData(a),inputData(b))

print(res)