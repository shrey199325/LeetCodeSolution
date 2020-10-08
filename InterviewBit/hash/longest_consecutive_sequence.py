"""
Longest Consecutive Sequence
Problem Description

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from the array A.



Problem Constraints
1 <= N <= 106

-106 <= A[i] <= 106



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the length of the longest set of consecutive elements from the array A.



Example Input
Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2:

 The set of consecutive elements will be [1, 2].
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        # O(NlogN) solution ->
        # if len(A) <= 1:
        #     return len(A)
        # A = sorted(A)
        # # print(A)
        # prev = A[0]
        # count = 1
        # ans = 1
        # for i in A[1:]:
        #     if prev+1 == i:
        #         count += 1
        #         prev = i
        #     elif prev != i:
        #         ans = max(ans, count)
        #         prev = i
        #         count = 1
        # return max(ans, count)
        # O(N) solution ->
        hMap = {}
        maxCount = 0
        for ele in A:
            if (hMap.get(ele) is None):
                lCount = 0
                rCount = 0
                if (hMap.get(ele - 1) is not None):
                    lCount = hMap[ele - 1]
                if (hMap.get(ele + 1) is not None):
                    rCount = hMap[ele + 1]
                hMap[ele] = lCount + 1 + rCount
                hMap[ele - lCount] = hMap[ele]
                hMap[ele + rCount] = hMap[ele]

                maxCount = max(maxCount, lCount + 1 + rCount)

        return maxCount