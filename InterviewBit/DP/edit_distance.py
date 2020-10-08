class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n = len(A)
        m = len(B)
        if n > m:
            A, B = B, A
            n, m = m, n
        dp = [[0 for _ in range(m + 1)] for __ in range(2)]
        dp[0] = [j for j in range(m + 1)]
        for i in dp: print(i)
        print()
        for i in range(1, n + 1):
            if i > 1:
                dp[0] = [k for k in dp[1]]
            for j in range(0, m + 1):
                if j == 0:
                    dp[1][j] = i
                elif A[i-1] != B[j-1]:
                    dp[1][j] = 1 + min(dp[0][j - 1], dp[0][j], dp[1][j - 1])
                else:
                    dp[1][j] = dp[0][j-1]
            for i in dp: print(i)
            print()
        return dp[-1][-1]


A = "aa"
B = "aaa"
ans = Solution().minDistance(A, B)
print(ans)

A = "sunday"
B = "saturday"
ans = Solution().minDistance(A, B)
print(ans)

A = "abac"
B = "aac"
ans = Solution().minDistance(A, B)
print(ans)