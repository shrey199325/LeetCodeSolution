class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        if len(A) <= 1:
            return [A]
        A.sort()
        return self.pm(A) + [[]] + [[A[0]]]

    def pm(self, A):
        # import pdb;pdb.set_trace()
        if len(A) <= 1:
            return [A]
        # if len(A) < 1:
        #     return []
        ans = []
        for i in range(len(A)):
            con = A[i+1:]
            temp = (self.pm(con))
            for j in temp:
                ans.append([A[i]] + j)
            # print(f"temp: {temp}, ans: {ans}, con: {con}")
            # ans.append(temp)
        for i in range(len(A)-1):
            con = A[:i-1]
            temp = (self.pm(con))
            for j in temp:
                ans.append([A[i]] + j)
            # print(f"temp: {temp}, ans: {ans}, con: {con}")
            # ans.append(temp)
        return ans


A = [12, 13]
A = [1,2,3]
# A = [1, 2, 3, 4]
print(Solution().subsets(A))