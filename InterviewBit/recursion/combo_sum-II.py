class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans = self.perm(A, B)
        return [] if ans == -1 else ans

    def perm(self, A, B):
        # import pdb; pdb.set_trace()
        if len(A) == 1:
            if B == A[0]:
                return [A]
            else:
                return -1
        prev = -1
        ans = []
        for i in range(len(A)):
            if A[i] > B:
                return ans
            if prev == -1:
                prev = A[i]
            elif A[i] == prev:
                continue
            else:
                prev = A[i]
            if A[i] == B:
                ans.append([B])
                return ans
            con = A[i + 1:]
            temp = self.perm(con, B - A[i])
            if temp != -1:
                for j in temp:
                    ans.append([A[i]] + j)
        return ans


A = [1,1,2,5,6,7,10]
B = 7
print(Solution().combinationSum(A, B))