# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/ 

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in sorted(nums, reverse = True):
            if -i in seen:
                return i
        return -1
        
""" Runtime 130 ms
Beats 96.33%
Memory 14.1 MB """        
