"""
Reverse string
"""


def solution(st):
    i = len(st) - 1
    out = ""
    while i >= 0:
        out += st[i]
        i -= 1
    return out


print(solution("ABCD"))
