class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        ls = 0
        for i in range(len(nums)):
            if ls == (s - nums[i] - ls):
                return i
            ls += nums[i]
            
        return -1
