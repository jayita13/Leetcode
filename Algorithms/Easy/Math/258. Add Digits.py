# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:        
        s=0
        while num>0:
            s+=num%10
            num//=10
            if num == 0 and s > 9:
                num = s
                s = 0
        return s
        
""" Runtime: 72 ms, faster than 7.32% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 54.40% of Python3 online submissions for Add Digits. """        
