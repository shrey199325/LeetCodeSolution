from typing import List, Set


class Solution:
    def uniqueSceneLength(self, A: List[str]) -> List[int]:
        ans: List[int] = []
        prev_index: int = 0
        scene_map: Set[str] = set()
        for ind, i in enumerate(A):
            if i in scene_map:
                ans.append(ind - prev_index)
                scene_map.clear()
                scene_map.add(i)
                prev_index = ind
            else:
                scene_map.add(i)
        ans.append(len(A) - prev_index)
        return ans


A = "a b a b c b a c a d e f e g d e h i j h k l i j"
A = A.split()
print(A)
print(Solution().uniqueSceneLength(A))