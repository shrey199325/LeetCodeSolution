"""
Spiral Order Matrix II
Problem Description

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Problem Constraints
1 <= A <= 1000



Input Format
First and only argument is integer A


Output Format
Return a 2-D matrix which consists of the elements in spiral order.



Example Input
Input 1:

1
Input 2:

2


Example Output
Output 1:

[ [1] ]
Output 2:

[ [1, 2], [4, 3] ]


Example Explanation
Explanation 1:


Only 1 is to be arranged.
Explanation 2:

1 --> 2
      |
      |
4<--- 3
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        mat = [[0 for _ in range(A)] for _ in range(A)]
        k, l, val = 0, 0, 1
        last_row, last_col = A - 1, A - 1
        while (k <= last_row and l <= last_col):
            for i in range(l, last_col + 1):
                mat[k][i] = val
                val += 1
            k += 1
            for i in range(k, last_row + 1):
                mat[i][last_col] = val
                val += 1
            last_col -= 1
            if k <= last_row:
                for i in range(last_col, l - 1, -1):
                    mat[last_row][i] = val
                    val += 1
                last_row -= 1
            if l <= last_col:
                for i in range(last_row, k - 1, -1):
                    mat[i][l] = val
                    val += 1
                l += 1
        return mat
