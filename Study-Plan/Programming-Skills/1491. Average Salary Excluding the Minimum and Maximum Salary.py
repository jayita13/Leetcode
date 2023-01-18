# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        sal = sorted(salary)[1:-1]
        return sum(sal)/len(sal)

""" Runtime 41 ms Beats 47.80%
Memory 13.8 MB Beats 94.94% """
