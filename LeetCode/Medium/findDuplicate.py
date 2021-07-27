"""
287. Find the Duplicate Number
Medium

7988

838

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sol_set = set()
        for num in nums:
            if sol_set:
                if num not in sol_set:
                    sol_set.add(num)
                else:
                    return num
            else:
                sol_set.add(num)


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        pass