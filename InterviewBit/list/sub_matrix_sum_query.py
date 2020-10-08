"""
Sub-matrix Sum Queries
Problem Description

Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom and columns are numbered from left to right.
Sum may be large so return the answer mod 109 + 7.


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M



Input Format
The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.



Output Format
Return an integer array containing the submatrix sum for each query.



Example Input
Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
Input 2:

 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]


Example Output
Output 1:

 [12, 28]
Output 2:

 [22, 19]


Example Explanation
Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.

"""


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        sum = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i + j == 0:
                    continue
                elif i == 0:
                    A[i][j] += A[i][j - 1]
                elif j == 0:
                    A[i][j] += A[i - 1][j]
                else:
                    A[i][j] += A[i][j - 1] + A[i - 1][j] - A[i - 1][j - 1]
        # print(A)
        for i in range(len(B)):
            x, y, a, b, temp = B[i] - 1, C[i] - 1, D[i] - 1, E[i] - 1, 0
            if x + y == 0 or a + b == 0:
                temp = A[a][b]
            elif a == 0 or x == 0:
                temp = A[a][b] - A[a][y - 1]
            elif y == 0 or b == 0:
                temp = A[a][b] - A[x - 1][b]
            else:
                temp = A[a][b] - A[a][y - 1] - A[x - 1][b] + A[x - 1][y - 1]
            sum.append(temp % (10 ** 9 + 7))

        return sum