"""
LIST
integer list,
[1,2,3,4,5,6,8,9]
Num=4
op: [4,3,2,1,9,8,6,5]

Num=6
[6,5,4,3,2,1,9,8]

A = [1,2,3,4,5,8,11]
NUM: 3
3,2,1,8,5,4,11
n = 7


i=min(num, len(A))
ans = []
A[i] to A[0]
i += num -> 6

"""
from typing import List


# A = [1,2,3,4,5] , num=3
def reverseInWindow(A: List[int], num: int) -> List[int]:
    if A is None or len(A) < 2:
        return A
    ans: List[int] = []
    n = len(A)  # 5
    i: int = min(num, n)  # 3
    prev = 0
    while i <= n:
        j = i-1  # 2
        while j >= prev:
            ans.append(A[j])
            j -= 1
        if i == n:
            break
        prev = i # 3
        i = min(i + num, n)  # 4
    return ans


A = [1, 2, 3, 4, 5]
print(reverseInWindow(A, 6))



"""
A = [12,3,2,1,15,1,7,8]
M = [15,15,15,15,15,8,8,8]
O = [   15,15,No,7,8,N]
A = [6,1,5,8]
M = [8,8,8,8]
O = [   ,8,N]
12->15
3->15
..
5->7
1->7
7->8
8->None

[]
"""

def nextGreatestElement(A):
    if A is None: print(None)
    n = len(A)
    M = [-1] * n
    prev_max = -1
    for i in range(n-1, -1, -1):
        if i == n-1:
            M[i] = A[i]
        else:
            M[i] = max(A[i], M[i+1])
    for i in range(n-1, -1, -1):
        if i == n-1:
            print("{} -> {}".format(A[i], None))
            prev_max = A[i]
        else:
            if A[i+1] > A[i]:
                print("{} -> {}".format(A[i], A[i+1]))
                prev_max = A[i+1]
            elif prev_max > A[i]:
                print("{} -> {}".format(A[i], prev_max))
            elif M[i] > A[i]:
                print("{} -> {}".format(A[i], M[i]))
            else:
                print("{} -> {}".format(A[i], None))


A = [2,5,1,7,8]
nextGreatestElement(A)