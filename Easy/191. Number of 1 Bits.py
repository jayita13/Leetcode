# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n).count("1")
        
''' Success Details 
Runtime: 53 ms, faster than 33.67% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.9 MB, less than 50.04% of Python3 online submissions for Number of 1 Bits. '''        
