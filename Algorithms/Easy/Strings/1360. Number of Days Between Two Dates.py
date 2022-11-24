# https://leetcode.com/problems/number-of-days-between-two-dates/

from datetime import datetime as dt
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((dt.strptime(date1, "%Y-%m-%d") - dt.strptime(date2, "%Y-%m-%d")).days)
        
""" Success Details 
Runtime: 46 ms, faster than 77.44% of Python3 online submissions for Number of Days Between Two Dates.
Memory Usage: 14 MB, less than 41.78% of Python3 online submissions for Number of Days Between Two Dates. """        
        
