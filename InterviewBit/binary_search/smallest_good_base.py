class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        for i in range(64, 1, -1):
            l = 2
            A = int(A)
            h = A - 1
            while l <= h:
                mid = (l + h) // 2
                s = ((mid ** i) - 1) // (mid - 1)
                # print(i, mid, s)
                if s == A:
                    return str(mid)
                if s < A:
                    l = mid + 1
                else:
                    h = mid - 1


print(Solution().solve("13"))
