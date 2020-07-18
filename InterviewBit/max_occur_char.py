"""
Max occurrence of a char
"""


class Solution:
    def solve(self, A: str, k: str):
        max_ = 0
        temp = 0
        i,j = 0,0
        for i in A:
            if i == k:
                temp += 1
            else:
                if max_ < temp:
                    temp = 0


A, k = input().split()  # input -> aabbaa a
Solution().solve(A, k)