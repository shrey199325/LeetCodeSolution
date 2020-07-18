"""
1175. Prime Arrangements
"""
class Solution(object):
    def fact(self, v):
        res = 1
        while v > 0:
            res *= v
            v -= 1
        return res

    def isPrime(self, v):
        if v % 2 == 0:
            return False
        for i in range(3, int(v ** 0.5) + 1, 2):
            if v % i == 0:
                return False
        return True

    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = 1
        for i in range(3, n + 1):
            prime = prime + 1 if self.isPrime(i) else prime
        return (self.fact(prime) * self.fact(n - prime)) % (10 ** 9 + 7)


class Solution2(object):
    def fact(self, v):
        res = 1
        while v > 0:
            res *= v
            v -= 1
        return res

    def SOE(self, n):
        res = n - 1
        prime = [False] * 2 + [True] * (n - 1)
        for i in range(2, n + 1):
            if prime[i]:
                j = 2
                while i * j <= n:
                    res = res - 1 if prime[i * j] else res
                    prime[i * j] = False
                    j += 1
        print(res)
        return res

    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = self.SOE(n)

        return (self.fact(prime) * self.fact(n - prime)) % (10 ** 9 + 7)