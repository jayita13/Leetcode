# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1

        return [i+1, j+1]

""" Runtime Details
123ms Beats 40.11%of users with Python3
Memory Details
17.20MB Beats 86.75%of users with Python3 """
