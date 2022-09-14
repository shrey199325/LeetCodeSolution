"""
90 degrees
    l     r
t   1,2,3,4
    5,6,7,8
    9,10,11,12
b   13,14,15,16



"""


def solution(arr, top=0, left=0, COL=4, ROW=4, sol=None):
    if not sol:
        sol = [[0 for _ in range(COL)] for __ in range(ROW)]
    right = COL - 1
    bottom = ROW - 1
    for i in range(left, right):
        sol[top+i][right] = arr[top][left+i]
        sol[bottom][right-i] = arr[top+i][right]
        sol[bottom-i][left] = arr[bottom][right-i]
        sol[top][left+i] = arr[bottom-i][left]
    top += 1
    left += 1
    COL -= 1
    ROW -= 1
    if top < COL and left < ROW:
        return solution(arr, top, left, COL, ROW, sol)
    else:
        return sol


def solution2(arr, top=0, left=0, COL=4, ROW=4):
    right = COL - 1
    bottom = ROW - 1
    for i in range(left, right):
        tmp1, tmp2, tmp3, tmp4 = arr[top + i][right], arr[bottom][right - i], arr[bottom - i][left], arr[top][left + i]
        arr[top + i][right] = tmp4
        arr[bottom][right - i] = tmp1
        arr[bottom - i][left] = tmp2
        arr[top][left + i] = tmp3
    top += 1
    left += 1
    COL -= 1
    ROW -= 1
    if top < COL and left < ROW:
        solution(arr, top, left, COL, ROW)


"""
1..100

"""


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
ans = [
    [13, 9, 5, 1],
    [14,10,6,2],
    [15,11,7,3],
    [16, 12, 8, 4]
]
print(solution(arr))

solution2(arr)
print(arr)

print(ans)