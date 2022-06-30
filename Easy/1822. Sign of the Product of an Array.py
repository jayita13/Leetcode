# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        for i in nums:
            p*=i
        
        if p>0:
            return 1
        elif p<0:
            return -1
        else:
            return 0
            
""" Success Details 
Runtime: 59 ms, faster than 96.99% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 13.9 MB, less than 98.02% of Python3 online submissions for Sign of the Product of an Array. """            
