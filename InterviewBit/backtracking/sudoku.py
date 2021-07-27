class Solution:
    # @param A : list of list of chars
    def solveSudoku(self, A):
        self.row, self.col, self.grid = (
            {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()},
            {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()},
            {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        )
        self.grid_first_element = {
            (0, 0): 1, (0, 3): 2, (0, 6): 3, (3, 0): 4, (3, 3): 5, (3, 6): 6, (6, 0): 7, (6, 3): 8, (6, 6): 9
        }
        A = [list(A[_]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == ".":
                    A[i][j] = 0
                else:
                    A[i][j] = int(A[i][j])
                    self.row[i + 1].add(A[i][j])
                    self.col[j + 1].add(A[i][j])
                    self.grid[self.calc_grid(i, j)].add(A[i][j])
        return self.recur(A, 0, 0)

    def recur(self, A, x, y):
        x, y = x+1, y+1
        for i in range(1, 10):
            if self.check(A, x, y, i):
                A[x][y] = i
                self.row[x].add(i)
                self.col[y].add(i)
                self.grid[self.calc_grid(x, y)].add(i)
                if x == y == 8:
                    return A
                if x < 8:
                    x_ = x + 1
                    y_ = y
                elif x == 8 and y < 8:
                    x_ = x
                    y_ = y + 1
                else: continue
                A = self.recur(A, x_, y_)
        return A

    def check(self, A, x, y, val):
        return val not in self.row[x] and val not in self.col[y] and val not in self.grid[self.calc_grid(x-1, y-1)]

    def calc_grid(self, x, y):
        top_left_row, top_left_col = (3 * (x // 3), 3 * (y // 3))
        return self.grid_first_element[(top_left_row, top_left_col)]


A = [
    "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"
]
print(Solution().solveSudoku(A))
