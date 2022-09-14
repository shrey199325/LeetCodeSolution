import sys


class RecursionDepth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)
        print("######## Set: ", self.limit)

    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)
        print("######## Set: ", self.default_limit)


def dfs(n, m):
    if n == m:
        print(n)
        return True
    print(n)
    return dfs(n+1, m)


with RecursionDepth(1005):
    print(dfs(1, 1002))
