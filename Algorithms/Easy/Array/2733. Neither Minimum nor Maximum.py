# https://leetcode.com/problems/neither-minimum-nor-maximum

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        # else:
        #     nums.remove(max(nums))
        #     nums.remove(min(nums))
        #     return nums[0]
        return sorted(nums)[1]

""" Runtime Details
338ms Beats 65.38%of users with Python3
Memory Details
16.07MB Beats 99.27%of users with Python3 """
