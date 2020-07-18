class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_li = len(nums)
        i, zero_count = 0, 0
        while i < len_li:
            if nums[i] != 0:
                i += 1
            else:
                zero_count += 1
                len_li -= 1
                nums.pop(i)

        nums.extend([0]*zero_count)

nums1 = [0,1,0,3,12]
Solution().moveZeroes(nums1)
print("Sol:")
print(nums1)