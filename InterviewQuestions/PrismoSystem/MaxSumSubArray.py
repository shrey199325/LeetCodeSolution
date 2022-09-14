"""

Given an integer array, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

input: nums = [-1,1,-3,4,-1,2,1,-5,4,-10,7]
output: 6
explanation: [4,-1,2,1] has the largest sum = 6



"""

from typing import List


def solution(nums: List[int]) -> int:
    max_ = max(nums)
    result = max_
    i = 0
    while i < len(nums):
        j = i + 1
        sum_ = nums[i]
        while j < len(nums):
            sum_ += nums[j]
            result = max(result, sum_)
            j += 1
        i += 1
    return result


nums = [-1,1,-3,4,-1,2,1,-7,7]

print(solution(nums))

# Time Complexity: O(n^2)
# Space Complexity: O(1)
