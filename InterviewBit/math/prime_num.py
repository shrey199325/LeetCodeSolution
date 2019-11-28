"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read Goldbach’s conjecture

Example:
Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

from datetime import datetime


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        isPrime = self.SOE(A)
        n = len(isPrime)
        for i in range(n):
            if (isPrime[i] == isPrime[-1 - i] == True):
                return [i, n - i - 1]

    def SOE(self, n):
        prime = [False] * 2 + [True] * (n - 1)
        for i in range(2, int(n**.5) + 1):
            if prime[i]:
                j = 2
                while i * j <= n:
                    prime[i * j] = False
                    j += 1
        return prime

before = datetime.now()
print(Solution().primesum(16777214))
after = datetime.now()
print(after-before)