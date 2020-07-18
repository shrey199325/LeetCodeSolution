class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if len(B) > len(A):
            return -1
        if len(A) == len(B):
            return 0 if A == B else -1
        mod_ = 10 ** 8
        needle = self.hashfn(B)
        prev_hash = 0
        p = 127
        for i in range(len(A) - len(B)):
            if i == 0:
                prev_hash = self.hashfn(A[:len(B)])
            else:
                prev_hash = (prev_hash // p + (self.hashfn(A[len(B) + i - 1]) * (p ** (len(B)-1))))
            if prev_hash == needle and B == A[i:len(B) + i]:
                return i
        return -1

    def hashfn(self, c):
        p = 127
        res = 0
        mod_ = 10 ** 8
        for index, i in enumerate(c):
            res += (ord(i) * (p ** index))
        return res


A = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
B = "babaaa"
print(Solution().strStr(A, B))
