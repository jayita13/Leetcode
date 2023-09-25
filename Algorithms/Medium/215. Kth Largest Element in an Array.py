# https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

""" Runtime Details
496ms Beats 49.10%of users with Python3
Memory Details
29.31MB Beats 80.71%of users with Python3 """
