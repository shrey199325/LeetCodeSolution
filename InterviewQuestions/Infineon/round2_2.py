"""
Given large pile of sticks of different sizes, pick up a stick of some length and then find at least
one pair of stick which when put together will match the size of the stick. Return no of times you can win.
Input : Given N no of sticks length of each stick Example Input 4 1,2,3,9 output - 1

arr = [1,2,3,4,5,6]
target = 6
out = 2
hset = {3}

"""


def solution(arr, target):
    hset = set()
    count_ = 0
    for i in arr:
        if i in hset:
            count_ += 1
        else:
            hset.add(target - i)
    return count_


arr = [1,2,3,4,5,6]
target = 6
print(solution(arr, target))
