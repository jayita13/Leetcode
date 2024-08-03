# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    s = max(s, (nums[i] - nums[j]) * nums[k])
        return s
