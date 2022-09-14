# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'getHeaviestPackage' function below.
# #
# # The function is expected to return a LONG_INTEGER.
# # The function accepts INTEGER_ARRAY packageWeights as parameter.
# #

def getHeaviestPackage(packageWeights):
    # Write your code here
    if len(packageWeights) == 1:
        return packageWeights[0]
    result = []
    prev_wt = packageWeights[-1]
    for i in range(len(packageWeights)-2, -1, -1):
        if packageWeights[i] < prev_wt:
            prev_wt += packageWeights[i]
        else:
            result.append(prev_wt)
    result.append(prev_wt)
    return max(result)



arr = [20,13,8,9]
print(getHeaviestPackage(arr))

arr = [30,15,7,9]
print(getHeaviestPackage(arr))

arr = [30,15,5,9]
print(getHeaviestPackage(arr))


print("next")


def getAllSublists(power):
    sum_ = 0
    for i in range(len(power)+1):
        for j in range(i+1, len(power)+1):
            sum_ += sum(power[i:j])*min(power[i:j])
    return sum_

def getAll(arr):
    ret = 0
    n = len(arr)
    for i in range(n):
        ret += min(arr[i:n]) * sum(arr[i:n])
    return ret




def findTotalPower(power):
    # Write your code here
    # sum_ = 0
    # sublists = getAllSublists(power)
    # for i in sublists:
    #     sum_ += (sum(i)*min(i))
    n = len(power)
    if n==0:
        return 0

    return (findTotalPower(power[0:n-1]) + getAll(power)) % 1000000007

arr = [2,3,2,1]
print(findTotalPower(arr))


