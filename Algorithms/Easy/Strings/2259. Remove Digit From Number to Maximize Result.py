# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s = ""
        for i,j in enumerate(number):
            if j == digit:
                s = max(s, number[:i]+number[i+1:])
        return s
            
        
""" Runtime
36 ms
Beats
40.70%
Memory
13.9 MB
Beats
8.59% """        
