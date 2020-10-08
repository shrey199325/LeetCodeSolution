"""
Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .

Conditions for a string to be balanced :

Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.


Problem Constraints
0 <= |A| <= 106



Input Format
First and only argument is an string A.



Output Format
Return an single integer denoting the lenght of the longest balanced substring.



Example Input
Input 1:

 A = "[()]"
Input 2:

 A = "[(])"


Example Output
Output 1:

 4
Output 2:

 0
"""

class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        if len(A) <= 1:
            return 0
        open_close = {"}": "{", "]": "[", ")": "("}
        stack = []
        occur = []
        dp = [0]*len(A)
        for ind, i in enumerate(A):
            if ind == 0:
                if i not in open_close.keys():
                    stack.append(i)
                    occur.append(ind)
            else:
                if i not in open_close.keys():
                    stack.append(i)
                    occur.append(ind)
                elif stack and open_close[i] == stack[-1]:
                    stack.pop()
                    prev_occur = occur.pop()
                    diff = ind - prev_occur + 1
                    dp[ind] = dp[ind-diff] + (diff)
                else:
                    stack = []
                    occur = []
        return max(dp)