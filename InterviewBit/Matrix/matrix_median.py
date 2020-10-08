"""
Matrix Median
Problem Description

Given a matrix of integers A of size N x M in which each row is sorted.

Find and return the overall median of the matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N, M <= 10^5

1 <= N*M <= 10^6

1 <= A[i] <= 10^9

N*M is odd



Input Format
The first and only argument given is the integer matrix A.



Output Format
Return the overall median of the matrix A.



Example Input
Input 1:

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ]
Input 2:

A = [   [5, 17, 100]    ]


Example Output
Output 1:

 5
Output 2:

 17


Example Explanation
Explanation 1:


A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.
Explanation 2:


Median is 17.
"""

from bisect import bisect_right


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def binSearch(self, matrix, min_el, max_el, cntElBeforeMed):
        start = min_el
        end = max_el
        while start < end:
            mid = start + ((end - start) // 2)
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, mid)
            if cnt > cntElBeforeMed:
                end = mid
            else:
                start = mid + 1

        return start

    def getMinMax(self, matrix):
        min_el = float('inf')
        max_el = float('-inf')
        for row in matrix:
            if min_el > row[0]:
                min_el = row[0]
            if max_el < row[-1]:
                max_el = row[-1]

        return min_el, max_el

    def findMedian(self, A):
        matrix = A
        rn = len(matrix)
        cn = len(matrix[0])
        cntElBeforeMed = (rn * cn) // 2
        min_el, max_el = self.getMinMax(matrix)
        return self.binSearch(matrix, min_el, max_el, cntElBeforeMed)


class Solution2:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        l, h = 1, 10 ** 9
        n, m = len(A), len(A[0])
        while l <= h:
            mid = (l + h) // 2
            same, greater, lesser = 0, 0, 0
            for i in range(n):
                l_index = 0
                g_index = self.greater_index(A[i], mid)
                # print(g_index)
                if g_index <= 1:
                    greater += (m if g_index == -1 else m-1)
                    same += (1 if A[i][0] == mid else 0)
                    lesser += (1 if A[i][0] < mid else 0)
                    continue
                l_index = self.lesser_index(A[i], g_index, mid)
                lesser += (l_index + 1)
                greater += (m - g_index)
                if l_index + 1 != g_index:
                    same += (g_index - l_index - 1)
            if same == 0:
                if lesser > greater:
                    h = mid - 1
                else:
                    l = mid + 1
            if lesser == greater or (0 < (greater - lesser) < same) or (0 < (lesser - greater) < same):
                return mid
            else:
                if lesser > greater:
                    h = mid - 1
                else:
                    l = mid + 1

    def greater_index(self, A, mid):
        l, h = 0, (len(A) - 1)
        if A[0] > mid:
            return -1
        elif A[-1] <= mid:
            return len(A)
        while l <= h:
            temp_mid = (l + h) // 2
            # print(l,temp_mid,h)
            if A[temp_mid-1] <= mid < A[temp_mid]:
                return temp_mid
            if A[temp_mid] > mid:
                h = temp_mid - 1
            elif A[temp_mid] <= mid:
                l = temp_mid + 1

    def lesser_index(self, A, m, mid):
        l, h = 0, (m - 1)
        if A[0] >= mid:
            return -1
        elif A[m-1] < mid:
            return m-1
        while l <= h:
            temp_mid = (l + h) // 2
            if A[temp_mid] < mid <= A[temp_mid + 1]:
                return temp_mid
            if A[temp_mid] >= mid:
                h = temp_mid - 1
            elif A[temp_mid] < mid:
                l = temp_mid + 1