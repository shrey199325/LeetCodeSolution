class MaxHeap:
    @staticmethod
    def heapify_up(a):
        if len(a) > 1:
            c = len(a) - 1
            while c > 0:
                root = c // 2 - 1 if c % 2 == 0 else c // 2
                if a[root] >= a[c]:
                    break
                a[root], a[c] = a[c], a[root]
                c = root

    @staticmethod
    def heapify_down(a):
        if len(a) > 1:
            root = 0
            while root < len(a):
                l = 2 * root + 1
                r = 2 * root + 2
                if (l >= len(a) and r >= len(a)) or ((l < len(a) and a[root] >= a[l]) and (
                        r < len(a) and a[root] >= a[r])) or (r >= len(a) and a[root] >= a[l]):
                    break
                c = l if r >= len(a) or a[l] >= a[r] else r
                a[root], a[c] = a[c], a[root]
                root = c

    @staticmethod
    def heap_pop(a):
        a[0], a[-1] = a[-1], a[0]
        res = a.pop()
        MaxHeap.heapify_down(a)
        return res

    @staticmethod
    def create_heap(a):  # max heap
        res = []
        for i in a:
            res.append(i)
            MaxHeap.heapify_up(res)
        return res


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        B = MaxHeap.create_heap(B)
        res = 0
        while B and (A > 0):
            temp = MaxHeap.heap_pop(B)
            res += temp
            B.append(temp // 2)
            MaxHeap.heapify_up(B)
            A -= 1
        return res


A = 5
B = [2, 4, 6, 8, 10]
print(Solution().nchoc(A, B))