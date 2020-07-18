def count_sq(A, DP, i):
    c = 0
    while i > 0:
        # print(i, i-1)
        c += A // DP[i - 1]
        A %= DP[i - 1]
        if A == 0:
            return c
        while A < DP[i - 1]: i -= 1
    return c


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        if A <= 2:
            return A
        root = 1
        while root * root <= A: root += 1
        root -= 1
        DP = [0] * root
        for i in range(1, root + 1):
            DP[i - 1] = i * i
        print(DP)
        print(root)
        i = root
        ans = A
        while i > 0:
            temp = count_sq(A, DP, i)
            print(temp)
            ans = min(ans, temp)
            i -= 1
        return ans

print(Solution().countMinSquares(97280))