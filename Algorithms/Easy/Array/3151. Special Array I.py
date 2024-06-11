# https://leetcode.com/problems/special-array-i

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def parity(num):
            if num % 2 == 1:
                return 'odd'
            else:
                return 'even'
        for i in range(1, len(nums)):
            if parity(nums[i]) == parity(nums[i-1]):
                return False
        return True

""" Runtime
65
ms
Beats
7.34%
of users with Python3
Memory
16.50
MB
Beats
95.42%
of users with Python3 """

