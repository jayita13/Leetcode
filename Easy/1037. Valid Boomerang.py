# https://leetcode.com/problems/valid-boomerang/

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        # straight line can't form triangle         
        area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
        return area != 0
        
''' Runtime: 50 ms, faster than 33.68% of Python3 online submissions for Valid Boomerang.
Memory Usage: 13.7 MB, less than 95.53% of Python3 online submissions for Valid Boomerang. '''        
