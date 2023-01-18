# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, L: int, R: int) -> int:
        N = (R - L) // 2
 
        # if either R or L is odd
        if (R % 2 != 0 or L % 2 != 0):
            N += 1
    
        return N

""" Runtime 36 ms Beats 60.3%
Memory 13.8 MB Beats 54.43% """
