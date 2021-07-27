"""
# write your code here...
# https://www.interviewbit.com/problems/painters-partition-problem/

# 10,20,30,40

# k=2

# k=1 => 10+20+30+40+1 = 100
# k=4 => 40

# 1<=k<=4
# 40<=ans<=100

# k-4 =>40 =>
# decrease => time increase.

# k-1 => 100
# k++ increase => time decrease

# 100+40/2 =
# (min. k) => 2

# Given Target No. of workers required.
# {
# for(int i = 0;i<n;i++)
# {
#     sum+=arr[i];
#     if( sum>=target)
#     {
#         k++;
#         sum = arr[i];
#     }
# }
# }
# 1
# 1
# 10 20 30 40

#k=2

https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Binary Indexed Tree
Apply
Segement Tree


from typing import List


def binarySearch(arr, p, l, h):
    while l < h:
        mid = l + (h-l)//2
        no_of_painters = 0
        sum_ = 0
        for i in range(len(arr)):
            sum_ =


def painterPartition(A: int, B: int, C: List[int]):
    max_ = C[0]
    sum_ = C[0]
    for i in C[1:]:
        max_ = max(max_, i)
        sum_ += i
    if len(C) <= A:
        return sum_*B
    if len(C) == 1:
        return max_*B
    return binarySearch(C, A, max_, sum_) * B



"""