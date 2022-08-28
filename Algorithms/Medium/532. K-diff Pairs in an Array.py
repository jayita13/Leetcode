# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num = []
        
        if k == 0: 
            nums = Counter(nums)
            return sum(v > 1 for k, v in nums.items())
        
        for i in nums:
            if i+k in nums:
                num.append(i+k) 
        
        return len(set(num))
