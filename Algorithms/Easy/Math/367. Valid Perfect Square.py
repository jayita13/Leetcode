# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) * sqrt(num) == num and sqrt(num) == int(sqrt(num))
        
""" Runtime
31 ms
Beats
70.24%
Memory
13.8 MB
Beats
42.71% """        
