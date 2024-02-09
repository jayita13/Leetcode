# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)    
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target) 

""" Runtime
43
ms
Beats
93.12%
of users with Python3
Memory
17.39
MB
Beats
68.43%
of users with Python3 """
