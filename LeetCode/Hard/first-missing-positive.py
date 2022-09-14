"""
41. First Missing Positive
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1, k, thres = 0, 0, (len(nums))
        for index, i in enumerate(nums):
            if i > 0 and i<=thres:
                val = 10 ** i
                res1 += val
        res1 //= 10
        while res1 % 10 != 0:
            res1 //= 10
            k += 1
        return k+1


class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        contains_one = False
        while i < len(nums):
            if nums[i] == 1:
                contains_one = True
            if 0 >= nums[i] or nums[i] > len(nums):
                nums[i] = 1
            i += 1
        print("Nums:", end=" ")
        print(nums)
        if not contains_one:
            return 1
        i = 0
        while i < len(nums):
            ind = nums[i] if nums[i] > 0 else -nums[i]
            if nums[ind-1] > 0:
                nums[ind-1] *= -1
            i += 1
        i = 1
        print("Nums2:", end=" ")
        print(nums, i)
        while i < len(nums):
            if nums[i] > 0:
                return i+1
            i += 1
        return i+1


nums = [1,-2,3,4,5]
print(Solution2().firstMissingPositive(nums), 6)
nums = [1]
print(Solution2().firstMissingPositive(nums), 2)
nums = [2]
print(Solution2().firstMissingPositive(nums), 1)
nums = [2456789]
print(Solution2().firstMissingPositive(nums), 1)
nums = [1,2,2]
print(Solution2().firstMissingPositive(nums), 3)
nums = [1,2,3,4,5,5]
print(Solution2().firstMissingPositive(nums), 6)
nums = [0,1,2,3,4,5,5]
print(Solution2().firstMissingPositive(nums), 6)
nums = [0,1,2,3,4,5,6]
print(Solution2().firstMissingPositive(nums), 7)
nums = [1,2,3,5,5]
print(Solution2().firstMissingPositive(nums), 4)
nums = [1,2,0]
print(Solution2().firstMissingPositive(nums), 3)
nums = [2147483647,100000,1,3,2,4,5,6,7,100001]
print(Solution2().firstMissingPositive(nums), 8)
nums = []
print(Solution2().firstMissingPositive(nums), 1)