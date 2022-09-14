"""
https://codecollab.io/@proj/HolidayHistoryCactus


# 4 - 4
# 8 - 4 8
# 6 - 4 6 8
# 2 - 2 4 6
# 9 - 2 4 6
# 1 - 1 2 4
# 3 - 1 2 3
n = 3
ans = [2, 4, 6]  if len(ans)<n
aux = [8, 6]
Def get_min(item):
	pass


Arr = [4, 8, 6, 2, 9, 1, 3]
For item iin arr:
	get_min(item)

"""

from typing import List


def addition(ans, num, aux, n):
    while ans and ans[-1] > num:
        aux.append(ans.pop())
    ans.append(num)
    while aux and len(ans) < n:
        ans.append(aux.pop())
    return ans


def get_item(num, n, ans) -> List[int]:
    aux = []
    if ans is None:
        return [num]
    if len(ans) == n and ans[-1] > num:
        ans.pop()
        return addition(ans, num, aux, n)
    if ans[-1] < num:
        ans.append(num)
        return ans
    return addition(ans, num, aux, n) if len(ans) < n else ans


A = [4, 8, 6, 2, 9, 1, 3]
n = 3
ans = None
for i in A:
    ans = get_item(i, n, ans)
    print(ans)
