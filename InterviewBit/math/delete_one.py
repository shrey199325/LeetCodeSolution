class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix, postfix = [A[0]], [A[-1]]
        n = len(A)
        if 1 <= n <= 2:
            return max(A)
        elif n == 0:
            return "Invalid Input"
        for i in range(1, n):
            prefix.append(self.gcd(prefix[-1], A[i]))
            postfix.append(self.gcd(postfix[-1], A[-(i + 1)]))
        max_ = -1
        # print(prefix, postfix)
        for i in range(1, n - 1):
            # print(prefix[i - 1], postfix[-(i + 2)])
            max_ = max(max_, self.gcd(prefix[i - 1], postfix[-(i + 2)]))
        # if len(prefix) >= 2:
        #     max_ = max(prefix[-2], max_)
        # if len(postfix) >= 2:
        #     max_ = max(postfix[1], max_)
        return max_

    def gcd(self, a, b):
        if a == b == 0:
            return 0
        if b == 0:
            return a
        return self.gcd(b, a % b)


print(Solution().solve([12, 15, 18]))
print(Solution().solve([21, 7, 3, 42, 63]))
print(Solution().solve([21, 7]))
