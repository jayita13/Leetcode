# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i%2==0:
                ans.insert(0,i)
            else:
                ans.insert(len(nums)-1, i)
        # for i in nums:
        #     if i%2!=0:
        #         ans.append(i)
        
        return ans 

''' Runtime: 116 ms, faster than 43.52% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 65.32% of Python3 online submissions for Sort Array By Parity. '''
