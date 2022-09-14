"""
    l l r r
t   1,2,3,4
t   5,6,7,8
b   9,10,11,12
b   13,14,15,16

"""


def solution(arr, left=0, top=0, COL=4, ROW=4):
    right = COL - 1
    bottom = ROW - 1
    i = top
    while i <= right:
        print(arr[top][i], end=" ")
        i += 1
    top += 1
    i = top
    while i <= bottom:
        print(arr[i][right], end=" ")
        i += 1
    right -= 1
    i = right
    while i >= left:
        print(arr[bottom][i], end=" ")
        i -= 1
    bottom -= 1
    i = bottom
    while i >= top:
        print(arr[i][left], end=" ")
        i -= 1
    left += 1
    print()
    if left <= right and top <= bottom:
        solution(arr, left, top, COL-1, ROW-1)


arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
solution(arr)