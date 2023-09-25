# https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        return sorted(set(nums))[-3]

""" Runtime Details
66ms Beats 13.17%of users with Python3
Memory Details
17.90MB Beats 15.33%of users with Python3 """
