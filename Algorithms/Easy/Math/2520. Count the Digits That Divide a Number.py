# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        c = 0 
        for i in str(num):
            if num % int(i) == 0:
                c += 1
        return c
        
""" Runtime 27 ms Beats 89.56%
Memory 13.8 MB Beats 90.85% """        
