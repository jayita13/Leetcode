# https://leetcode.com/problems/find-the-middle-index-in-array/
# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums)
        for i in range(len(nums)):
            rs -= nums[i]
            if ls == rs:
                return i
            ls += nums[i]
            
        return -1
    
#       Alternate but can give TLE
#         j, k = 0, 1
        
#         for i in range(len(nums)):
#             sl, sr = 0, 0
#             sl += sum(nums[:j])
#             j+=1
#             sr += sum(nums[k:])
#             k+=1
#             if sl == sr:
#                 return i

#         return -1
        
""" Success Details 
Runtime: 76 ms, faster than 23.50% of Python3 online submissions for Find the Middle Index in Array.
Memory Usage: 13.8 MB, less than 95.93% of Python3 online submissions for Find the Middle Index in Array. """        
