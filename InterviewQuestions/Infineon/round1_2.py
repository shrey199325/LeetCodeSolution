"""
sorted positive array
integer x
arr = [1,2,3,4,5,6,7,8,9]
x = 10
hset = {}
out -> [1,9]
"""


def solution(arr, x):
    hset = set()
    i = 0
    sol = []
    while i < len(arr):
        if arr[i] in hset:
            sol.append([x-arr[i], arr[i]])
        else:
            hset.add(x - arr[i])
        i += 1
    return sol


arr1 = [1,2,3,4,5,6,7,8,9]
x1 = 10
print(solution(arr1, x1))
