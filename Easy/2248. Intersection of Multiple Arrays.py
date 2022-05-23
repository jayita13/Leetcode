# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        f=0
        if len(nums)==1:
            return sorted(nums[0])
        for i in nums[0]:
            for j in range(1,len(nums)):
                if i in nums[j]:
                    f=1
                else:
                    f=0
                    break
            if f:
                ans.append(i)
        
        return sorted(ans)
