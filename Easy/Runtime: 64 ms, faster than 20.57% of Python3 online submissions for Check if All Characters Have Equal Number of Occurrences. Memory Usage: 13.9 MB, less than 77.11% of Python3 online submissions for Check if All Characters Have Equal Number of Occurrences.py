# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s1=[]
        for i in range(len(s)):
            s1.append(s.count(s[i]))
            
        return len(set(s1))==1                   

''' Runtime: 64 ms, faster than 20.57% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.
Memory Usage: 13.9 MB, less than 77.11% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences. '''
