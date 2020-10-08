class Solution:
    # @param a : integer
    # @param b : integer
    # @return an integer
    def gcd(self, a, b):
        if a == b == 0:
            return 0
        if b == 0:
            return a
        return self.gcd(b, a % b)
