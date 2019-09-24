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
        while res1%10!=0:
            res1 //= 10
            k += 1
        return k+1

nums = [1,2,3,4,5]
print(Solution().firstMissingPositive(nums))
nums = [1]
print(Solution().firstMissingPositive(nums))
nums = [2]
print(Solution().firstMissingPositive(nums))
nums = [2456789]
print(Solution().firstMissingPositive(nums))
nums = [1,2,2]
print(Solution().firstMissingPositive(nums))
nums = [1,2,3,4,5,5]
print(Solution().firstMissingPositive(nums))
nums = [1,2,3,5,5]
print(Solution().firstMissingPositive(nums))
nums = [1,2,0]
print(Solution().firstMissingPositive(nums))
nums = [2147483647,100000,1,3,2,4,5,6,7,100001]
print(Solution().firstMissingPositive(nums))
nums = []
print(Solution().firstMissingPositive(nums))