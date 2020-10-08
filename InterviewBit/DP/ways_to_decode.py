"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.

Problem Constraints
1 <= length(A) <= 105

Input Format
The first and the only argument is a string A.

Output Format
Return an integer, representing the number of ways to decode the string modulo 109 + 7..

Example Input
Input 1:

 A = "12"
Input 2:

 A = "8"


Example Output
Output 1:

 2
Output 2:

 1
"""


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        MOD = (10**9 + 7)
        dp = [0]*len(A)
        if A[0] > "0":
            dp[0] = 1
            if len(A) == 1: return 1
        else: return 0
        if A[1] > "0":
            dp[1] = 1
        if 0 < int(A[:2]) <= 26:
            dp[1] += 1
        elif A[1] == 0: return 0
        for i in range(2, len(A)):
            decode = int(A[i])
            if decode != 0:
                dp[i] = (dp[i] + dp[i-1])
            decode = int(A[i-1:i+1])
            if A[i-1] != "0" and 0 < decode <= 26:
                dp[i] = (dp[i] + dp[i-2])
        return dp[-1] % MOD


A = "2611"
print(Solution().numDecodings(A))