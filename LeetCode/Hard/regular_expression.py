# write your code here...
# https://leetcode.com/problems/regular-expression-matching/

"""
aaa
a*
* -> dp[i-1][j-1]


a*
a

0 , 1, ...*

cb*
b

dp[i][j-2]

if( p[i-1] == s[j-1] || p[i-1] == '.')
    dp[i][j] = dp[i-1][j-1]
else if(p[i-1] == '*')
    dp[i][j] = dp[i-2][j]
    if(s[j-1] == p[i-2] || p[i-1] == '.')
    {
        dp[i][j]= dp[i][j] or dp[i][j-1]
    }



else if( s[i-1] != p[j-1])
    dp[i][j] = F

=T

---
dp[i][j] = if p[i-1]==s[j-1]
   "" a a a
"" T  F F F
a  F  T F F
*  T  T
"""


# Incorrect
class Solution:
    def isMatch(self, s, p):
        if p == ".*":
            return True
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True # empty string
        if p[0] == ".":
            dp[1][0] = True
        for i in range(1, m+1):
            # 0th column
            if p[i-1] == "*":
                dp[i][0] = dp[i-2][0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] == s[j-1] or p[i-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    dp[i][j] = dp[i-1][j]
                    if p[i-3] == s[j-1] or p[i-3] == ".":
                        dp[i][j] = dp[i][j] or dp[i-2][j]
        for i in dp: print(i)
        return dp[-1][-1]

"""
         0 1 2
      "" a a a
   "" T  F F F
0  a  F  T F F
1  b  F  f f f
2  *  F  t f f
3  a  F  
4  c  F
5  *  F
6  a  F

   "" a a
"" T  F F
a  F  t f
*  T  t 
"""


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        form = [[False for _ in range(len(p) + 1)] for __ in range(len(s) + 1)]
        form[0][0] = True # empty
        for j in range(2, len(p) + 1):
            form[0][j] = self.check("", p[j - 1], p[j - 2], False, False, form[0][j - 2])
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                p_prev = p[j - 2] if j >= 2 else ""
                lefter = form[i][j - 2] if j >= 2 else False
                form[i][j] = self.check(s[i - 1], p[j - 1], p_prev, form[i - 1][j - 1],
                                        form[i - 1][j], lefter)
        # print(form)
        return form[-1][-1]

    def check(self, s: str, p: str, p_prev: str, prev: bool, up: bool, lefter: bool) -> bool:
        if s == p or p == ".":
            return prev
        elif p == "*":
            if s == p_prev or p_prev == ".":
                return lefter or up
            return lefter
        else:
            return False

# s="aa"
# p = "a*"
s = "aab"
p = "c*a*b"
s = ["aaa", "aab", "aa"]
p = ["ab*ac*a", "c*a*b", "a*"]

for s1, p1 in zip(s, p):
    print(Solution().isMatch(s1, p1))