class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if B < C:
            B, C = C, B
        if B % C == 0:
            pass