# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        left = []
        right = []
        ans = []
        for i in range(len(nums)):
            left.append(sum(nums[:i]))
        for i in range(len(nums)):
            right.append(sum(nums[i+1:]))
        for i in range(len(nums)):
            ans.append(abs(left[i]-right[i]))
        return ans
        
        
