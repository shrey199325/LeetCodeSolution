"""
Given an array of integers,
find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order.

Brute force would be to sort the array and remove duplicates.
then check for longest subsequence
O(nlogn) due to sorting
"""


def solution_bf(arr):
    if arr is None:
        return 0
    if len(arr) <= 1:
        return len(arr)
    arr.sort()
    no_dups = []
    for i in range(len(arr)):
        if i == 0:
            no_dups.append(arr[i])
        elif arr[i] != no_dups[-1]:
            no_dups.append(arr[i])
    i = 1
    res = 1
    curr_subseq_count = 1
    while i < len(no_dups):
        if no_dups[i-1] + 1 == no_dups[i]:
            curr_subseq_count += 1
        else:
            res = max(curr_subseq_count, res)
            curr_subseq_count = 1
        i += 1

    return res


"""
Optimal solution would be to add it to a set and and then check the whole array for starting points.
This would be in O(n)
"""


def solution_op(arr):
    if arr is None:
        return 0
    if len(arr) <= 1:
        return len(arr)
    no_dups = set()
    max_ = max(arr)
    res = 0
    for i in arr:
        if i not in no_dups:
            no_dups.add(i)
    for i in arr:
        if i-1 not in no_dups:
            # starting point
            count = 1
            for j in range(i+1, max_+1):
                if j in no_dups:
                    count += 1
                else:
                    break
            res = max(res, count)
    return res


arr = [1,9,3,10,4,20,2]
print(solution_bf(arr))
print(solution_op(arr))
arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
print(solution_bf(arr))
print(solution_op(arr))
