# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        s = 9999
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        s = min(s, nums[i] + nums[j] + nums[k])
        if s != 9999:
            return s
        else:
            return -1

""" Runtime 73
ms
Beats
24.09%
Memory
16.52
MB
Beats
35.75%      """
