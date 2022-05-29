# https://leetcode.com/problems/set-mismatch/

# from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # ans = []
        # ans.append(list((Counter(nums)-Counter(set(nums))).keys())[0])
        # n = len(nums)
        # ans.append((n*(n+1))//2 - sum(set(nums))) 
        # return ans
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]

            
