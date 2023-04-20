# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        for i,j in enumerate(str(n)):
            if i % 2 == 0:
                s+=int(j)
            else:
                s+=-1*int(j)
        return s

""" Runtime 20 ms Beats 98.3%
Memory 13.8 MB Beats 39.4% """
