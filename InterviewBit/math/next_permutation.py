"""
Next Permutation
Problem Description

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

NOTE:

The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.


Problem Constraints
1 <= N <= 5 * 105

1 <= A[i] <= 109



Input Format
The first and the only argument of input has an array of integers, A.



Output Format
Return an array of integers, representing the next permutation of the given array.



Example Input
Input 1:

 A = [1, 2, 3]
Input 2:

 A = [3, 2, 1]


Example Output
Output 1:

 [1, 3, 2]
Output 2:

 [1, 2, 3]


Example Explanation
Explanation 1:

 Next permutaion of [1, 2, 3] will be [1, 3, 2].
Explanation 2:

 No arrangement is possible such that the number are arranged into the numerically next greater permutation of numbers.
 So will rearranges it in the lowest possible order.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        split_index = self.get_split_index(A)
        if split_index == -1:
            self.reverse(A, 0)
        else:
            change_index = self.get_change_index(A, split_index)
            self.swap(A, split_index, change_index)
            self.reverse(A, split_index + 1)
        return A

    def reverse(self, A, start):
        left = start
        right = len(A) - 1
        while left < right:
            self.swap(A, right, left)
            left += 1
            right -= 1

    def get_split_index(self, A):
        i = len(A) - 1
        while i > 0:
            if A[i] < A[i - 1]:
                i -= 1
            else:
                break
        return i - 1

    def get_change_index(self, A, i):
        j = len(A) - 1
        while j >= i:
            if A[j] > A[i]:
                break
            else:
                j -= 1
        return j

    def swap(self, A, i, j):
        A[i], A[j] = (A[j], A[i])