# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
        
''' Success Details 
Runtime: 176 ms, faster than 56.59% of Python3 online submissions for Single Number.
Memory Usage: 16.9 MB, less than 20.51% of Python3 online submissions for Single Number. '''        
