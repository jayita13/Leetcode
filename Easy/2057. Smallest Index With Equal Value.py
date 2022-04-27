# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                res = i
                break
            else:
                res = -1
        return res
        
''' Runtime: 128 ms, faster than 36.25% of Python3 online submissions for Smallest Index With Equal Value.
Memory Usage: 13.9 MB, less than 10.27% of Python3 online submissions for Smallest Index With Equal Value. '''        
