# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c, d, e = [], [], []
        for i in range(1, a+1):
            if a % i == 0:
                c.append(i)
        for i in range(1, b+1):
            if b % i == 0:
                d.append(i)
        
        for i in c:
            if i in d:
                e.append(i)
        
        return len(e)
        
""" Runtime: 74 ms, faster than 9.07% of Python3 online submissions for Number of Common Factors.
Memory Usage: 13.9 MB, less than 63.01% of Python3 online submissions for Number of Common Factors. """        
