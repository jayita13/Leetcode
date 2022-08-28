# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for num in nums:
            if len(str(num))%2==0:
                c+=1
        return c
                
''' Runtime: 103 ms, faster than 16.51% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 14 MB, less than 51.30% of Python3 online submissions for Find Numbers with Even Number of Digits. '''
