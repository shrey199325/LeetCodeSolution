"""
Sub-array with 0 sum
Problem Description

Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1 else return 0.



Problem Constraints
1 <= |A| <= 100000

-10^9 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return whether the given array contains a subarray with a sum equal to 0.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [-1, 1]


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 No subarray has sum 0.
Explanation 2:

 The array has sum 0.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        set_ = set()
        prefix_sum = []
        for i in A:
            prefix_sum.append(i if len(prefix_sum) == 0 else i + prefix_sum[-1])
        for i in prefix_sum:
            if i not in set_ and i != 0:
                set_.add(i)
            else:
                return 1
        return 0