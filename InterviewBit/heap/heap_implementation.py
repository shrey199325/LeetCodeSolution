from typing import List

VECTOR = List[int]


class MinHeap:
    @staticmethod
    def heapify_up(a: VECTOR):
        if len(a) > 1:
            c = len(a) - 1
            while c > 0:
                root = c // 2 - 1 if c % 2 == 0 else c // 2
                if a[root] <= a[c]:
                    break
                a[root], a[c] = a[c], a[root]
                c = root

    @staticmethod
    def heapify_down(a: VECTOR):
        if len(a) > 1:
            root = 0
            while root < len(a):
                l = 2 * root + 1
                r = 2 * root + 2
                if (l >= len(a) and r >= len(a)) or (l < len(a) and a[root] <= a[l]) and (
                        r < len(a) and a[root] <= a[r]):
                    break
                c = l if a[l] <= a[r] else r
                a[root], a[c] = a[c], a[root]
                root = c

    @staticmethod
    def heap_pop(a: VECTOR):
        a[0], a[-1] = a[-1], a[0]
        res = a.pop()
        MinHeap.heapify_down(a)
        return res

    @staticmethod
    def create_heap(a: VECTOR):  # min heap
        res = []
        for i in a:
            res.append(i)
            MinHeap.heapify_up(res)
        return res


class MaxHeap:
    @staticmethod
    def heapify_up(a: VECTOR):
        if len(a) > 1:
            c = len(a) - 1
            while c > 0:
                root = c // 2 - 1 if c % 2 == 0 else c // 2
                if a[root] >= a[c]:
                    break
                a[root], a[c] = a[c], a[root]
                c = root

    @staticmethod
    def heapify_down(a: VECTOR):
        if len(a) > 1:
            root = 0
            while root < len(a):
                l = 2 * root + 1
                r = 2 * root + 2
                if (l >= len(a) and r >= len(a)) or (l < len(a) and a[root] >= a[l]) and (
                        r < len(a) and a[root] >= a[r]):
                    break
                c = l if a[l] >= a[r] else r
                a[root], a[c] = a[c], a[root]
                root = c

    @staticmethod
    def heap_pop(a: VECTOR):
        a[0], a[-1] = a[-1], a[0]
        res = a.pop()
        MaxHeap.heapify_down(a)
        return res

    @staticmethod
    def create_heap(a: VECTOR):  # min heap
        res = []
        for i in a:
            res.append(i)
            MaxHeap.heapify_up(res)
        return res


q = [1, 10, 20, 30, 5, 6]
q = MinHeap.create_heap(q)
print(q)
res = MinHeap.heap_pop(q)
print(res, q)

q = [1, 10, 20, 30, 5, 6]
q = MaxHeap.create_heap(q)
print(q)
res = MaxHeap.heap_pop(q)
print(res, q)
