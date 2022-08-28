# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = dict()
        f = 0
        
        for i in nums:
            freq[i] = freq.get(i,0) + 1
            
        for i,j in freq.items():
            if j == len(nums)//2:
                f = i
                break

''' Runtime: 252 ms, faster than 63.67% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.6 MB, less than 12.26% of Python3 online submissions for N-Repeated Element in Size 2N Array. '''
