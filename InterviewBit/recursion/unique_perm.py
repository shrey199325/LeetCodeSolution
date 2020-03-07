class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) <= 1:
            return [A]
        A.sort()
        return self.pm(A)

    def pm(self, A):
        # import pdb; pdb.set_trace()
        if len(A) == 1:
            return [A]
        ans = []
        prev = None
        for i in range(len(A)):
            if prev is None or prev != A[i]:
                prev = A[i]
            else:
                continue
            con = [A[j] for j in range(len(A)) if j != i]
            temp = self.pm(con)
            for j in temp: ans.append([A[i]] + j)
        return ans


A = [0, 0, 0, 1, 9]
# A = [1,1,2]
C = (Solution().permute(A))
B = [[0, 0, 0, 1, 9, ], [0, 0, 0, 9, 1, ], [0, 0, 1, 0, 9, ], [0, 0, 1, 9, 0, ], [0, 0, 9, 0, 1, ], [0, 0, 9, 1, 0, ], [0, 1, 0, 0, 9, ], [0, 1, 0, 9, 0, ], [0, 1, 9, 0, 0, ], [0, 9, 0, 0, 1, ], [0, 9, 0, 1, 0, ], [0, 9, 1, 0, 0, ], [1, 0, 0, 0, 9, ], [1, 0, 0, 9, 0, ], [1, 0, 9, 0, 0, ], [1, 9, 0, 0, 0, ], [9, 0, 0, 0, 1, ], [9, 0, 0, 1, 0, ], [9, 0, 1, 0, 0, ], [9, 1, 0, 0, 0, ]]
print(C)
if len(C) == len(B):
    for i in C:
        if i not in B:
            print(False)
print(True)