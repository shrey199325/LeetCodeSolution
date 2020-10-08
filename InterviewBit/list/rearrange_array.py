"""
Rearrange the array
Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)].

Rearrange the array such that A[i] = j is changed to A[j] = i for all i and j form 0 to N-1.

Note: Try solving this with O(1) extra space.


Input Format

The only argument given is the integer array A.
Output Format

Return the rearranged array A.
Constraints

1 <= N <= 100000
0 <= A[i] < N
For Example

Input 1:
    A = [1, 2, 3, 4, 0]
Output 1:
    [4, 0, 1, 2, 3]

Input 2:
    A = [2, 0, 1, 3]
Output 2:
    [1, 2, 0, 3]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        max_ = n
        for i in range(n):
            j = A[i] if A[i] < max_ else A[i] // max_ - 1
            temp = A[j] if A[j] < max_ else A[j] // max_ - 1
            A[j] = max_ * (temp+1) + i
        for i in range(n):
            A[i] = A[i] % max_
        return A