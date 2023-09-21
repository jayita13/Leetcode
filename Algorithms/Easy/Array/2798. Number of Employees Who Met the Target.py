# https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        s = 0
        for i in hours:
            if i >= target:
                s += 1
        return s

""" Runtime Details
44ms Beats 79.59%of users with Python3
Memory Details
16.18MB Beats 90.27%of users with Python3 """
