"""
arr = [
    [1,2,3,4],
    [12,13,14,15],
    [23,24,25,26],
    [34,35,36,37]
]
target = 24
"""


def solution(arr, target):
    rows, cols = len(arr), len(arr[0])
    top = 0
    right = cols - 1

    while top < rows and right >= 0:
        if arr[top][right] == target:
            return top, right
        elif arr[top][right] < target:
            top += 1
        else:
            right -= 1
    return -1


arr = [
    [1,2,3,4],
    [12,13,14,15],
    [23,24,25,26],
    [34,35,36,37]
]
target = 100

print(solution(arr, target))