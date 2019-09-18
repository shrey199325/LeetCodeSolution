"""
26. Remove Duplicates from Sorted Array
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = 0
        if nums:
            prev = nums[0]
            ll = 1
            for i in nums:
                if i==prev:
                    continue
                prev = i
                nums[ll] = i
                ll += 1
            nums = nums[:ll]
        return ll