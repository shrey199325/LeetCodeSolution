"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurance = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for index, c in enumerate(S):
            j = max(j, last_occurance[c])
            if index == j:
                ans.append(index - anchor + 1)
                anchor = index + 1

        return ans
