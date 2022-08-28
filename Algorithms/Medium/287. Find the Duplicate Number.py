# https://leetcode.com/problems/find-the-duplicate-number/

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return list((Counter(nums)-Counter(set(nums))).keys())[0]
        
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return nums[i]

