# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    c+=1
        
        return c
        
''' Runtime: 128 ms, faster than 83.56% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 15.1 MB, less than 10.95% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix. '''        
