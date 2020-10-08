"""
5070. Shortest Distance to Target Color
"""


class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        col_len = len(colors) # 5
        for i, j in queries:
            # 4, 2
            found = False
            loop_count = max(col_len-i, i)
            if colors[i] == j:
                res.append(0)
                continue
            for k in range(1, loop_count):
                if (i-k) >= 0 and colors[i-k] == j:
                    found = True
                    res.append(k)
                    break
                elif (i+k) < len(colors) and colors[i+k] == j:
                    found = True
                    res.append(k)
                    break
            if not found:
                res.append(-1)

        return res

print(Solution().shortestDistanceColor(colors=[1, 1, 2, 1, 3, 2, 2, 3, 3], queries=[[1, 3], [2, 2], [6, 1]]))
print(Solution().shortestDistanceColor([2,1,2,2,1], [[1,1],[4,3],[1,3],[4,2],[2,1]]))
# Solution().shortestDistanceColor()
# Solution().shortestDistanceColor()



"""
1,2,3,4,5,3,2,1
"""