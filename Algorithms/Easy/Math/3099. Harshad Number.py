# https://leetcode.com/problems/harshad-number/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        b = x
        s = 0
        while x > 0:
            s += x % 10
            x = x//10
        if b % s == 0:
            return s
        else: 
            return -1
          
""" Runtime  34 ms Beats 59.31%
Memory 16.40 MB Beats 96.74% """
