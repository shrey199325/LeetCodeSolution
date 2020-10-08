"""
Rain Water Trapped
Problem Description

Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
First and only argument is the vector A



Output Format
Return one integer, the answer to the question



Example Input
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

1 unit is trapped on top of the 3rd element.
Explanation 2:

No water is trapped.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        total = 0
        if len(A) <= 2:
            return total
        prefix_max = A[0]
        postfix_max = [0] * (len(A) - 1)
        # without the last element
        postfix_max[-1] = A[-1]
        for i in range(len(A) - 3, -1, -1):
            postfix_max[i] = A[i + 1] if A[i + 1] >= postfix_max[i + 1] else postfix_max[i + 1]
        for i in range(1, len(A) - 1):
            if A[i] < prefix_max and A[i] < postfix_max[i]:
                total += (min(prefix_max, postfix_max[i]) - A[i])
            prefix_max = A[i] if A[i] > prefix_max else prefix_max
        return total
