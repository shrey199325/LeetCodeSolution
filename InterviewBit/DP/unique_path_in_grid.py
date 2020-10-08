"""
Unique Paths in a Grid
Problem Description

Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.



Problem Constraints
1 <= n, m <= 100
A[i][j] = 0 or 1



Input Format
Firts and only argument A is a 2D array of size n * m.



Output Format
Return an integer denoting the number of unique paths from (1, 1) to (n, m).



Example Input
Input 1:

 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:

 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]


Example Output
Output 1:

 2
Output 2:

 0


Example Explanation
Explanation 1:

 Possible paths to reach (n, m): {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)} and {(1 ,1), (2, 1), (3, 1), (3, 2), (3, 3)}
 So, the total number of unique paths is 2.
Explanation 2:

 It is not possible to reach (n, m) from (1, 1). So, ans is 0.
"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        n = len(A)
        m = len(A[0])
        if A[0][0] == 1:
            return 0
        dp = [[0 for _ in range(m)] for __ in range(n)]
        print(dp)
        dp[0][0] = 1
        for j in range(1, m):
            if A[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, n):
            for j in range(m):
                if j == 0 and A[i][j] != 1:
                    dp[i][j] = dp[i - 1][j]
                elif A[i][j] != 1:
                    if A[i - 1][j] != 1:
                        dp[i][j] += dp[i - 1][j]
                    if A[i][j - 1] != 1:
                        dp[i][j] += dp[i][j - 1]
        print(dp)
        return dp[-1][-1]


class Solution2:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        n = len(A)
        m = len(A[0])
        if A[0][0] == 1:
            return 0
        dp = [[0 for _ in range(m)] for __ in range(min(2, n))]
        print(dp)
        dp[0][0] = 1
        for j in range(1, m):
            if A[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, n):
            if i > 1:
                dp[0] = [k for k in dp[1]]
            for j in range(m):
                if j == 0 and A[i][j] != 1:
                    dp[1][j] = dp[0][j]
                elif A[i][j] != 1:
                    if A[i - 1][j] != 1:
                        dp[1][j] += dp[0][j]
                    if A[i][j - 1] != 1:
                        dp[1][j] += dp[1][j - 1]
        print(dp)
        return dp[-1][-1]

# print(Solution2().uniquePathsWithObstacles([[0]]))

A = [
  [0, 0],
  [0, 0],
  [0, 0],
  [1, 0],
  [0, 0]
]

print(Solution().uniquePathsWithObstacles(A))
print(Solution2().uniquePathsWithObstacles(A))