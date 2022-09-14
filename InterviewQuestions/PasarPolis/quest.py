"""
A = [1,0,0,0,1,0,0]
zeroCountBegin = True
zeroCount = 0

op: 1, 3
"""


def maxZeroCount(A):
    if A is None or len(A) == 0:
        return 0, -1
    zeroCountBegin = False
    tempZeroCount, tempFirstZeroIndex = 0, -1
    zeroCount, zeroIndex = 0, -1
    map = dict()
    for index, i in enumerate(A):
        if i == 0:
            if not zeroCountBegin:
                zeroCountBegin = True
                tempFirstZeroIndex = index
            tempZeroCount += 1
        elif zeroCountBegin:
            zeroCountBegin = False
            map[tempFirstZeroIndex] = tempZeroCount
            if zeroCount < tempZeroCount:
                zeroCount = tempZeroCount
                zeroIndex = tempFirstZeroIndex
            tempZeroCount, tempFirstZeroIndex = 0, -1
    if zeroCountBegin:
        if 0 in map:
            tempZeroCount += map[0]
        if zeroCount < tempZeroCount:
            return tempFirstZeroIndex, (tempFirstZeroIndex+tempZeroCount-1) % (len(A))
    return zeroIndex, zeroIndex+zeroCount-1



A = [0, 0, 1, 0, 0, 1, 0, 1]
print(maxZeroCount(A))