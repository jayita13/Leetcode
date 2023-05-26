# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s = max(nums)
        ind = nums.index(s)
        for _ in range(1, k):
            score = max(nums)        
            new_score = score + 1
            nums[ind] = new_score
            s += new_score 
        return s
        
