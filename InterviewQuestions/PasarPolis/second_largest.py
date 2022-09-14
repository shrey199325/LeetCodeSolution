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


ZERO = "0"


def is_greater_than(str1: str, str2: str) -> bool:
    """
    Equivalent to expression str1 > str2
    """
    if (str1 > ZERO > str2) or (str1 == ZERO and ZERO > str2) or (str1 > ZERO and str2 == ZERO):
        # if str1 is a positive string integer or equal to "0" and str2 is a negative string integer
        return True
    if (str1 < ZERO < str2) or (str1 == str2) or (str1 == ZERO and str2 < ZERO) or (str1 < ZERO and str2 == ZERO):
        # if str1 is a negative string integer and str2 is a positive string integer or equal to "0"
        #  or if both strings are equal
        return False
    if str1 > ZERO:
        # This condition would be true only if both strings are positive string integers
        if len(str1) > len(str2) or (len(str1) == len(str2) and str1 > str2):
            return True
        return False
    if len(str1) < len(str2) or (len(str2) == len(str2) and str1 < str2):
        # This condition would be executed only if both strings are positive string integers
        return True
    return False


class Solution:
    def larger_element_check(self, curr_elem: str, max1: str, max2: str) -> Tuple[str, str]:
        if max1 is None or is_greater_than(curr_elem, max1):
            max2, max1 = max1, curr_elem
        elif is_greater_than(max1, curr_elem) and (max2 is None or is_greater_than(curr_elem, max2)):
            max2 = curr_elem
        return max1, max2

    def second_largest_element(self, arr: List[str]) -> int:
        if arr is None or len(arr) < 2:
            return -1
        max1, max2 = None, None
        for i in arr:
            max1, max2 = self.larger_element_check(i, max1, max2)
        return int(max2) if max2 is not None else -1


# Below are a list of queries in the form of a tuple.
# 1st element of the tuple represents the query
# 2nd element represents the expected answer
queries: List[Tuple[List[str], int]] = [
    (None, -1),
    ([], -1),
    (["-214748364801", "-214748364802"], -214748364802),
    (["-214748364801", "-214748364801"], -1),
    (["5", "5", "4", "2"], 4),
    (["3", "-2"], -2),
    (["3", "-4", "-4"], -4),
    (["3", "-2", "1"], 1),
    (["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], 9),
    (["11000", "11000", "10001", "10002", "10003", "10004", "10001", "10000"], 10004)
]
# The solution is called on all the queries and the answer is printed. For example, (["1", "2", "3"], 2) would print:
# Actual Value: 2, Expected Value: 2, Result -> True
for query, expected in queries:
    actual = Solution().second_largest_element(query)
    print(f"Actual Value: {actual}, Expected Value: {expected}, Result -> {actual == expected}")
# The output of queries:
# Actual Value: -1, Expected Value: -1, Result -> True
# Actual Value: -1, Expected Value: -1, Result -> True
# Actual Value: -214748364802, Expected Value: -214748364802, Result -> True
# Actual Value: -1, Expected Value: -1, Result -> True
# Actual Value: 4, Expected Value: 4, Result -> True
# Actual Value: -2, Expected Value: -2, Result -> True
# Actual Value: -4, Expected Value: -4, Result -> True
# Actual Value: 1, Expected Value: 1, Result -> True
# Actual Value: 9, Expected Value: 9, Result -> True
# Actual Value: 10004, Expected Value: 10004, Result -> True