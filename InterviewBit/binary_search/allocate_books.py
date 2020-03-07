class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        max_ = max(A)
        l, h, min_ = max_, sum(A), min(A)
        result = -1
        while l <= h:
            mid = (l + h) // 2
            temp_max = l
            possible = True
            print(min_, l, mid, h, temp_max)
            j = 0
            for i in range(B):
                sum_ = 0
                if (j >= (len(A) - 1) and i != (B - 1)) or j > (len(A) - 1):
                    possible = False
                    print("breaking: {}, {}".format(i, j))
                    break
                if i == (B - 1):
                    while j < len(A):
                        sum_ += A[j]
                        j += 1
                else:
                    while j < len(A):
                        if (sum_ + A[j]) <= mid:
                            sum_ += A[j]
                            j += 1
                        else:
                            break
                print(i, sum_, temp_max)
                temp_max = max(sum_, temp_max)
            if possible and result == -1:
                result = temp_max
                print("result: {}".format(result))
                h = result - 1
            elif possible:
                if result > temp_max:
                    result = temp_max
                    h = result - 1
                    print("result: {}".format(result))
                else:
                    l = mid + 1
            else:
                h = mid - 1
        if result == -1:
            if len(A) >= B:
                return max_
        return result


# A = [97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24]
# B = 26
# A = [ 23, 6, 13, 70, 38, 94, 20, 44, 66, 34, 26, 94, 63, 38, 44, 90, 50, 59, 23, 47, 85, 17, 72, 39, 47, 85 ]
# B = 7
# A = [ 61, 25, 35, 68, 95, 76, 67, 39, 74, 31, 56, 1, 72, 60, 94, 84, 55, 89, 7 ]
# B = 8
# A = [ 53, 83, 47, 7, 73, 22, 5, 76, 53, 24 ]
# B = 6
# A = [ 18, 0, 89, 62, 54, 63, 43, 89, 50, 35, 15, 64, 94, 63, 58, 52, 92, 16, 14, 20, 60, 50 ]
# B = 6
A = [ 51, 86, 31, 44, 39, 76, 84, 52, 8, 14, 54, 19, 28, 71, 70, 63, 47, 24, 43, 54, 8, 81, 52, 88, 63, 59, 19, 79 ]
B = 7
print(Solution().books(A, B))
