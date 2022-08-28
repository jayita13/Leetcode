# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        maxi = max(nums)
        ind = nums.index(maxi)
        nums.remove(maxi)
        for i in range(len(nums)):
            if maxi < 2*nums[i]:
                return -1
        
        return ind
