"""
1. 1st positive no. -> i , j = i-1 (last negative number)  == Binary search
abs(j) < i -> sq jth elem = ans -> j--
3
-2
"""

def firstPositiveNumber(A):
    """
    A: list[int]
    return: int
    """
    if len(A) > 0 and A[0] > 0:
        return 0
    if len(A) > 0 and A[-1] < 0:
        return len(A)
    l = 0
    h = len(A)-1
    while l <= h:
        mid = l + (h-l) // 2
        if A[mid] > 0 and A[mid-1] < 0:
            return mid
        elif A[mid] > 0:
            h = mid - 1
        else:
            l = mid + 1

def sortedSquares(A):
    """
    A: list[int]
    return: list[int]
    """
    if len(A) == 0:
        return []
    if len(A) == 1:
        return [A[0]*A[0]]
    i = firstPositiveNumber(A)
    ans = []
    j = i-1 if i > 0 else -1
    while i < len(A) or j >= 0:
        if j >= 0 and i < len(A):
            if -A[j] < A[i]:
                ans.append(A[j]*A[j])
                j -= 1
            else:
                ans.append(A[i]*A[i])
                i += 1
        elif j >= 0:
            ans.append(A[j]*A[j])
            j -= 1
        else:
            ans.append(A[i]*A[i])
            i += 1
    return ans