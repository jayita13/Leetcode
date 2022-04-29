# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        if len(set(nums)) == 1:
            return nums
            
        arr = sorted(nums, reverse=True)
        for i in range(len(arr)):
            if sum(arr[:i]) > sum(arr[i:]):
                return arr[:i]
