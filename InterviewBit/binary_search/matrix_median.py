class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        if len(A) == 1:
            return A[0][len(A[0]) // 2]
        l, h = 1, 10 ** 9
        n, m = len(A), len(A[0])
        while l <= h:
            mid = (l + h) // 2
            same, greater, lesser = 0, 0, 0
            for i in range(n):
                g_index = self.greater_index(A[i], mid)
                # print(g_index)
                if g_index <= 1:
                    greater += (m if g_index == -1 else m-1)
                    same += (1 if A[i][0] == mid else 0)
                    lesser += (1 if A[i][0] < mid else 0)
                    print(i, l, mid, h, lesser, -1, same, greater, g_index)
                    continue
                l_index = self.lesser_index(A[i], g_index, mid)
                lesser += (l_index + 1)
                greater += (m - g_index)
                if l_index + 1 != g_index:
                    same += (g_index - l_index - 1)
                print(i, l, mid, h, lesser, l_index, same, greater, g_index)
            if same == 0:
                if lesser > greater:
                    h = mid - 1
                else:
                    l = mid + 1
            if lesser == greater or (0 < (greater - lesser) < same) or (0 < (lesser - greater) < same):
                return mid
            else:
                if lesser > greater:
                    h = mid - 1
                else:
                    l = mid + 1

    def greater_index(self, A, mid):
        l, h = 0, (len(A) - 1)
        if A[0] > mid:
            return -1
        elif A[-1] <= mid:
            return len(A)
        while l <= h:
            temp_mid = (l + h) // 2
            # print(l,temp_mid,h)
            if A[temp_mid-1] <= mid < A[temp_mid]:
                return temp_mid
            if A[temp_mid] > mid:
                h = temp_mid - 1
            elif A[temp_mid] <= mid:
                l = temp_mid + 1

    def lesser_index(self, A, m, mid):
        l, h = 0, (m - 1)
        if A[0] >= mid:
            return -1
        elif A[m-1] < mid:
            return m-1
        while l <= h:
            temp_mid = (l + h) // 2
            # print(l, temp_mid, h, A[temp_mid], mid)
            if A[temp_mid] < mid <= A[temp_mid + 1]:
                return temp_mid
            if A[temp_mid] >= mid:
                h = temp_mid - 1
            elif A[temp_mid] < mid:
                l = temp_mid + 1


#     0 1  2  3  4  5  6  7  8  9  10
# li = [1,20,30,40,50,60,70,80,80,90,90]
# print(Solution().lesser_index(li, 6, 70))

# A = [
#   [1, 3, 5],
#   [2, 6, 9],
#   [3, 6, 9]
# ]
A = [
  #0      1       2       3       4       5       6       7       8       9       10
  [95479, 128929, 140681, 159665, 159665, 159665, 202532, 219458, 219458, 219511, 250456],
  [95479, 128929, 140681, 140681, 159665, 198431, 198431, 202532, 219511, 250456, 250456],
  [32984, 95479, 128929, 128929, 140681, 159665, 202532, 219458, 219458, 219511, 250456],
]
A = [
  [1, 1, 2, 9, 10, 12, 12, 17, 21, 22, 30],
  [2, 3, 5, 7, 8, 12, 21, 25, 26, 27, 30],
  [1, 3, 12, 13, 13, 14, 17, 18, 21, 21, 23]
]
# A = [
#   [5],
#   [4],
#   [3],
#   [1],
#   [3],
#   [1],
#   [4],
#   [2],
#   [5],
#   [3],
#   [3]
# ]
# A = [
#   [1, 16, 19],
#   [5, 12, 17],
#   [5, 27, 29]
# ]
print(Solution().findMedian(A))
# print(Solution().greater_index(A[0], 159665))
# print(Solution().lesser_index(A[0], 6, 159665))
# print(Solution().greater_index(A[0], 12))
# print(Solution().lesser_index(A[0], 7, 12))
#     0 1  2  3  4  5  6  7  8  9  10
# li = [1,20,30,40,50,60,70,80,80,90,90]
# print(Solution().greater_index(li, 75))
# print(Solution().lesser_index(li, 7, 75))