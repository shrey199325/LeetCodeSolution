"""
Maximum Consecutive Gap
Problem Description

Given an unsorted integer array A of size N.
Find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
Return 0 if the array contains less than 2 elements.



Problem Constraints
1 <= N <= 106

1 <= A[i] <= 109



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the maximum difference.



Example Input
Input 1:

 A = [1, 10, 5]
Input 2:

 A = [10, 9, 10]


Example Output
Output 1:

 5
Output 2:

 1


Example Explanation
Explanation 1:

 After sorting, the array becomes [1, 5, 10]
 Maximum difference is (10 - 5) = 5.
Explanation 2:

 Maximum difference is (10 - 9) = 1.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if n<2: return 0
        Min = min(A)
        Max = max(A)
        gap = (Max-Min)/float(n-1)
        if gap==0: return 0
        MIN = Min-1
        MAX = Max+1
        elems = [[MIN, MAX] for i in range(n)] # stores (min, max) for every gap range
        for num in A:
            pos = int((num-Min)/gap)
            elems[pos][0] = max(elems[pos][0], num)
            elems[pos][1] = min(elems[pos][1], num)
        # print gap, elements
        ans = 0
        prev = elems[0][1] # Which would ofcourse be Min
        for i in range(n):
            if elems[i][0]==MIN and elems[i][1]==MAX:
                continue # These gap range doesn't have any elements
            ans = max(ans, elems[i][1]-prev)  # (min of this range) - (max of prev)
            prev = elems[i][0]   # Max for this gap range
        return ans