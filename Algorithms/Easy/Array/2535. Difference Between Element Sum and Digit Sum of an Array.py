# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = sum(nums)
        digi_sum = 0        
        for i in nums:
            s = 0
            mod = 0 
            while i>0:
                mod = i%10
                s += mod
                i = i//10
            digi_sum += s
        return abs(ele_sum - digi_sum)
        
""" Runtime 120 ms Beats 96.52%
Memory 14.2 MB Beats 47.13% """         
