"""
5068. Before and After Puzzle
"""


class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        len_p = len(phrases)
        res = set()
        for i in range(len_p):
            if phrases[i]:
                for j in range(len_p):
                    if i==j:
                        continue
                    if phrases[j]:
                        if phrases[i].split(" ")[-1]==phrases[j].split(" ")[0]:
                            sec = phrases[j].split(" ")[1:]
                            sol = phrases[i]+" "+" ".join(sec) if sec else phrases[i]
                            res.add(sol)
                    else:
                        res.add(phrases[i])
        return sorted(res)



# print Solution().beforeAndAfterPuzzles(["a","b","a"])
# print Solution().beforeAndAfterPuzzles(["writing code","code rocks"])
res =  Solution().beforeAndAfterPuzzles(["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"])


abc = ["a quick bite to eat my words","a man on a mission statement","chocolate bar of soap","a chip off the old block party","a man on a mission impossible"]

print res
print abc