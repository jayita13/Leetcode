# https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for a in range(int(sqrt(c))+1):
            b = sqrt(c-a*a)
            if b == int(b):
                return True

""" Runtime
118 ms
Beats
77.68%
Memory
16.2 MB
Beats
41.70%  """
