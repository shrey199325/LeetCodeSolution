"""
Delete one
Problem Description

Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.



Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the maximum value of GCD.



Example Input
Input 1:

 A = [12, 15, 18]
Input 2:

 A = [5, 15, 30]


Example Output
Output 1:

 6
Output 2:

 15


Example Explanation
Explanation 1:


 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum vallue of gcd is 6.
Explanation 2:

 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix, postfix = [A[0]], [A[-1]]
        n = len(A)
        if 1 <= n <= 2:
            return max(A)
        elif n == 0:
            return "Invalid Input"
        for i in range(1, n):
            prefix.append(self.gcd(prefix[-1], A[i]))
            postfix.append(self.gcd(postfix[-1], A[-(i + 1)]))
        max_ = -1
        for i in range(1, n - 1):
            max_ = max(max_, self.gcd(prefix[i - 1], postfix[-(i + 2)]))
        return max_

    def gcd(self, a, b):
        if a == b == 0:
            return 0
        if b == 0:
            return a
        return self.gcd(b, a % b)