# https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = sorted(heights)
        c = 0
        for i, j in zip(heights, res):
            if i!=j:
                c+=1
        return c
        
''' Runtime: 60 ms, faster than 29.37% of Python3 online submissions for Height Checker.
Memory Usage: 13.9 MB, less than 57.06% of Python3 online submissions for Height Checker. '''        
