"""    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
arr = [1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3]
       l            m                r
arr = [1]
       l r m     r
target = 1
"""


def firstOccurence(arr, target):
    l = 0
    r = len(arr) - 1
    # res = r + 1
    res = -1
    while l <= r:
        m = l + ((r-l) // 2)
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            # res = min(res, m)
            # r = m - 1
            res = max(res, m)
            l = m + 1
    # return res if res < len(arr) else -1
    return res


arr = [1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3]
target = 3
print(firstOccurence(arr, target))