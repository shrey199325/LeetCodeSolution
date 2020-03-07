class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) <= 1:
            return [A]
        return self.pm(A)

    def pm(self, A):
        if len(A) == 1:
            return A
        ans = []
        for i in range(len(A)):
            con = [A[j] for j in range(len(A)) if j != i]
            # print(f"A: {A}, con: {con}")
            temp = self.pm(con)
            if len(temp) == 1:
                temp = [temp]
            # print(f"temp: {temp}")
            for j in temp: ans.append([A[i]] + j)
        return ans

A = [1,2,3]
print(Solution().permute(A))
