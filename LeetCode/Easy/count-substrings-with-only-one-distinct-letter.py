"""
5067. Count Substrings with Only One Distinct Letter
"""
class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        dict_s = {}
        i = 0
        while i < len(S):
            prev, count = S[i], 0
            while i < len(S) and S[i]==prev:
                count += 1
                i += 1
            s = S[i-1] * count
            for k in range(0, count):
                    if s[k:] in dict_s: dict_s[s[k:]] += k+1
                    else: dict_s[s[k:]] = k+1

        return sum(dict_s.values())

print Solution().countLetters("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrhhhhnnn")

print Solution().countLetters("aabba")