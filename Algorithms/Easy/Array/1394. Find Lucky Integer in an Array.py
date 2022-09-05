# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen =  []
        for i in arr:
            if arr.count(i) == i:
                seen.append(i)
        if len(seen):
            return max(set(seen))
        else:
            return -1

""" Runtime: 137 ms, faster than 14.45% of Python3 online submissions for Find Lucky Integer in an Array.
Memory Usage: 13.9 MB, less than 49.86% of Python3 online submissions for Find Lucky Integer in an Array. """
