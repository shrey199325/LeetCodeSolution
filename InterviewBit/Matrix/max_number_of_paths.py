"""
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
0<=m,n<=100
"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        res = self.total_unique_paths(A, 0, 0) if A[0][0] == 0 else 0
        return res

    def total_unique_paths(self, A, x, y):
        res1, res2 = 0, 0
        if x == len(A) - 1 and y == len(A[0]) - 1 and A[x][y] == 0:
            return 1
        if x < len(A) - 1 and y <= len(A[0]) - 1:
            if A[x + 1][y] == 0:
                res1 = self.total_unique_paths(A, x + 1, y)
        if x <= len(A) - 1 and y < len(A[0]) - 1:
            if A[x][y + 1] == 0:
                res2 = self.total_unique_paths(A, x, y + 1)
        return res1 + res2
