# https://leetcode.com/problems/find-the-maximum-achievable-number/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t

""" Runtime Details
42ms Beats 64.22%of users with Python3
Memory Details
16.33MB Beats 21.76%of users with Python3 """
