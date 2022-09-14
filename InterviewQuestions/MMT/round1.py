"""
sequence of number
Write a program which takes as input a very long sequence of numbers and prints the numbers in sorted order.
Each number is at most k away from its correctly sorted position.
For example, no number in sequence [3, -1, 2, 6, 4, 5, 8] is more than 2 away from its final sorted position
arr, k
k {1, 100}
arr -> {1, 10**6}
op = [-1, 2, 3, 4, 5, 6, 8]
arr = [3, -1, 2, 6, 4, 5, 8], k = 2
       0  1   2  3  4  5  6
       L      k  l     k
       -1 2 3 4 6 5 8
       2k+1
"""
import heapq


def solution(arr, k):
    if len(arr) < 2:
        return arr
    k_heap = []
    out = []

    for i in range(0, len(arr)-(2*k) + 1, k+1):
        j = min(2*(k+i) + 1, len(arr))
        l = i
        k_heap = arr[i:j]
        heapq.heapify(k_heap)  # k
        while l <= i+k:
            out.append(heapq.heappop(k_heap))  # klogk
            l += 1
    while k_heap:
        out.append(heapq.heappop(k_heap))
    return out


def solution2(arr, k):
    k_heap = arr[0:k+1]
    heapq.heapify(k_heap)
    out = []
    for i in range(k+1, len(arr)):
        out.append(heapq.heappop(k_heap))
        heapq.heappush(k_heap, arr[i])
    while k_heap:
        out.append(heapq.heappop(k_heap))
    return out


arr = [3, -1, 2, 6, 4, 5, 8]
k = 2
print(solution(arr, k))
print(solution2(arr, k))
