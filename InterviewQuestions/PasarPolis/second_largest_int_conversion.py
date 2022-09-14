"""
Write a function which takes an array of integers given as string as an argument and returns
second max value from the input array. If there is no second max return -1.

let's take some examples:

1. For array ["3", "-2"] should return "-2"
2. For array ["5", "5", "4", "2"] should return "4"
3. For array ["4", "4", "4"] should return -1 (duplicates are not considered as the second max)
4. For [] (empty array) should return -1.
5. For ["-214748364801","-214748364802"] should return -214748364802.

Restrictions :
1. CPU complexity should be O(n)
2. You are not allowed to change the array
3. Maximum length of the integer string can be 2^10=1024 digits
"""
from typing import List, Tuple

MIN_VAL = float("-inf")


class Solution:
    def largerElementCheck(self, curr_elem: int, max1: int, max2: int) -> Tuple[int, int]:
        if curr_elem > max1:
            max2, max1 = max1, curr_elem
        elif max1 > curr_elem > max2:
            max2 = curr_elem
        return max1, max2

    def secondLargestElement(self, arr: List[str]) -> int:
        if arr is None or len(arr) < 2:
            return -1
        max1, max2 = MIN_VAL, MIN_VAL
        for i in arr:
            max1, max2 = self.largerElementCheck(int(i), max1, max2)
        return max2 if max2 != MIN_VAL else -1


qs: List[Tuple[List[str], int]] = [
    (None, -1),
    ([], -1),
    (["-214748364801", "-214748364802"], -214748364802),
    (["-214748364801", "-214748364801"], -1),
    (["5", "5", "4", "2"], 4),
    (["3", "-2"], -2),
    (["3", "-4", "-4"], -4),
    (["3", "-2", "1"], 1),
    (["11000", "11000", "10001", "10002", "10003", "10004", "10001", "10000"], 10004)
]
for q, expected in qs:
    actual = Solution().secondLargestElement(q)
    print(actual == expected)
