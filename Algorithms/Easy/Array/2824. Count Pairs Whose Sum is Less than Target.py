# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        s = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    s += 1
        return s

""" 
Runtime Details
56ms Beats 55.75%of users with Python3
Memory Details
16.29MB Beats 66.33%of users with Python3
"""      
            
