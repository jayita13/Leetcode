# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
        return l

""" Runtime Details
2917ms Beats 12.48%of users with Python3
Memory Details
16.93MB Beats 98.33%of users with Python3 """
