# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                s += nums[i]**2
        return s

""" Runtime
Details
65ms
Beats 70.57%of users with Python3
Memory
Details
16.04MB
Beats 93.42%of users with Python3 """
