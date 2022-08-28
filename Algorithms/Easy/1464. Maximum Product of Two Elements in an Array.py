# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      
        # max1 = max(nums)
        # nums.remove(max1)
        # max2 = max(nums)
        # return (max1-1)*(max2-1)
        
        new = sorted(nums) 
        max1 = new[-1]
        max2 = new[-2]
        return (max1-1)*(max2-1)
      
'''Runtime: 68 ms, faster than 62.32% of Python3 online submissions for Maximum Product of Two Elements in an Array.
Memory Usage: 13.9 MB, less than 52.86% of Python3 online submissions for Maximum Product of Two Elements in an Array.'''
