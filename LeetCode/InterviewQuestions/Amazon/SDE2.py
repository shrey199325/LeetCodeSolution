"""
1.
i / p:
    str = ABDCDGOYXITC
    k = 3
o / p:
    The number of sub string that does not have repeating characters.

Solution:
    TC: O(n)
    SC: O(k)
    char_count = dict()
    GDGA
    {
        D: 1
        G: 2
        O: 1
    }
    substr = str[0:k]
    ans = 3

    i = 0->n - k
    char_count = dict()
    {
        C: 2
        D: 1
    }
    multi_char = {C}
    ans = 1
"""


def numberOfNonRepeatCharInWindow(S, k):
    """
    S: str
    k: int
    return: int
    """
    S = "ABCCDECDGOYXITC"
    k = 3
    if S is None or k is not None or len(S) < k or k <= 0:
        return 0
    char_count = dict()
    multi_char = set()
    ans = 0
    for i in range(k):
        if S[i] not in char_count:
            char_count[S[i]] = 1
        else:
            char_count[S[i]] += 1
            multi_char.add(S[i])
    if not multi_char:
        ans += 1
    for i in range(1, len(S) - k):
        if S[i - 1] in multi_char:
            char_count[S[i - 1]] -= 1
            if char_count[S[i - 1]] == 0:
                char_count.pop(S[i - 1])
                multi_char.pop(S[i - 1])
        else:
            char_count.pop(S[i - 1])
        if S[i + k] not in char_count:
            char_count[S[i + k]] = 1
        else:
            char_count[S[i + k]] += 1
            multi_char.add(S[i + k])
        if not multi_char:
            ans += 1
    return ans


"""
2. Level order traversal in a line.

2 - 0
4
5 - 1
6
8
2 - 2
queue = (node, 0)
ans = [[2], [4, 5], [6, 8, 2]]
while queue:
    child, ht = queue.pop()
    ans[ht]
    append(child.val)
    queue = (child, ht + 1)
print: 2
4
5
6
8
2
"""
