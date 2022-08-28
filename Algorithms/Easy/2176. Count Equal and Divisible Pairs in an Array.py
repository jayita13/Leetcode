# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)): 
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    c+=1
        return c
        
'''Runtime: 147 ms, faster than 34.41% of Python3 online submissions for Count Equal and Divisible Pairs in an Array.
Memory Usage: 13.9 MB, less than 24.60% of Python3 online submissions for Count Equal and Divisible Pairs in an Array.'''
