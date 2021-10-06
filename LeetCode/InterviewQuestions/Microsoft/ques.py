# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def incrementor(n, m, left, right, up, down, shift):
    n, m = abs(n), abs(m)
    if right:
        return (n+1, m-1, left, False, up, True) if shift else (n, m+1, left, right, up, down)
    if down:
        return (n-1, m-1, True, right, up, False) if shift else (n+1, m, left, right, up, down)
    if left:
        return (n-1, m-1, False, right, True, down) if shift else (n, m-1, left, right, up, down)
    if up:
        return (n-1, m+1, left, True, False, down) if shift else (n-1, m, left, right, up, down)


def solution(R):
    # write your code in Python 3.6
    cleaned = 0
    if len(R) == 0 or len(R[0]) == 0 or R[0][0] == "X":
        return cleaned
    if len(R) == 1 and "X" not in R[0]:
        return len(R[0])
    covered = set()
    n, m = 0, 1
    covered.add((n, m))
    right, down, left, up = True, False, False, False
    covered_once = False
    #print(n, m)
    while True:
        shift =  n == len(R) or n < 0 or m == len(R[0]) or m < 0 or R[n][m] == "X"
        n, m, left, right, up, down = incrementor(n, m, left, right, up, down, shift)
        #print(n,m, covered)
        cond =  n >= len(R) or n < 0 or m >= len(R[0]) or m < 0 or R[n][m] == "X"
        if cond:
            covered_once = False
            continue
        if (n, m) in covered:
            if covered_once:
                break
            covered_once = True
        else:
            covered.add((n, m))
            covered_once = False
    return len(covered)







