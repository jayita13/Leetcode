# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:        
        return gcd(min(nums),max(nums))

'''Runtime: 52 ms, faster than 98.04% of Python3 online submissions for Find Greatest Common Divisor of Array.
Memory Usage: 14.1 MB, less than 49.24% of Python3 online submissions for Find Greatest Common Divisor of Array.'''
