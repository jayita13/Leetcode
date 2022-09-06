# https://leetcode.com/problems/missing-number/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s+t:
            res^=ord(i)
        return chr(res)
        
''' Success Details 
Runtime: 51 ms, faster than 45.49% of Python3 online submissions for Find the Difference.
Memory Usage: 13.9 MB, less than 32.95% of Python3 online submissions for Find the Difference. '''
