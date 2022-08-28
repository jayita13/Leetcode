# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        
        for i in s.split(" "):
            if i.isnumeric():
                nums.append(int(i))
                
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1] or nums[i]==nums[i+1]:
                return False
            else:
                continue
                
        return True

''' Success Details 
Runtime: 29 ms, faster than 94.46% of Python3 online submissions for Check if Numbers Are Ascending in a Sentence.
Memory Usage: 13.9 MB, less than 59.70% of Python3 online submissions for Check if Numbers Are Ascending in a Sentence.'''
