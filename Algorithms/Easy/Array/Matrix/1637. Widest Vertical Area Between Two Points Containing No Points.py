# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for i in range(1, len(points)):
            ans = max(ans, points[i][0] - points[i-1][0])
        return ans

""" Runtime
774
ms
Beats
15.51%
of users with Python3
Memory
59.19
MB
Beats
96.11%
of users with Python3 """
