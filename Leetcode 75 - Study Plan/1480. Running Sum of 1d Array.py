class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            ans.append(s)
        return ans
        
