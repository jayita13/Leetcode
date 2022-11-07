# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2 

""" Success Details 
Runtime: 63 ms, faster than 19.52% of Python3 online submissions for Smallest Even Multiple.
Memory Usage: 13.8 MB, less than 50.77% of Python3 online submissions for Smallest Even Multiple. """
