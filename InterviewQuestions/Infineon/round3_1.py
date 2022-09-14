"""
string = "abc"
out -> abc, acb, bac, bca, cab, cba
"""


def permutations(s):
    if not s:
        return [""]
    if len(s) < 2:
        return [s]
    if len(s) == 2:
        return [s, s[::-1]]
    res = set()
    for i in range(len(s)):
        first_str = s[i]
        out = []
        out.extend(permutations(s[:i] + s[i+1:]))
        for combo in out:
            res.add(first_str + combo)
    return res


print(permutations("abb"))