class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        len_mat_row = len(matrix)
        len_mat_col = len(matrix[0])
        j, k, m, n = 0, 0, 0, 0
        res = []
        total_range = len_mat_row*len_mat_col
        for i in range(total_range):
            if j==m and k<(len_mat_col-1-n):
                res.append(matrix[j][k])
                k+=1
            elif j<(len_mat_row-1-m) and k==(len_mat_col-1-n):
                res.append(matrix[j][k])
                j += 1
            elif j==(len_mat_row-1-m) and k>n:
                res.append(matrix[j][k])
                k -= 1
            elif j>(m+1) and k==n:
                res.append(matrix[j][k])
                j -= 1
                if j==(m+1): m+=1; n+=1
            else:
                res.append(matrix[j][k])
        return res


class Sol2(object):
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(mat))
print(Sol2().spiralOrder(mat))