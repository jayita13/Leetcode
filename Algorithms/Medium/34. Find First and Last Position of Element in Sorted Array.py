# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        else:
            ans = sorted(nums)
            l = ans.index(target)
            r = len(ans) - 1 - ans[::-1].index(target)
            return [l, r]

""" Runtime 75ms Beats 73.28% of users with Python3
Memory 17.87 MB Beats 70.11% of users with Python3 """      
