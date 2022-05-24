# https://leetcode.com/problems/percentage-of-letter-in-string/

import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        if letter not in s:
            return 0
        c=0       
        for i in s:
            if letter == i:
                c+=1
        return math.floor(c/len(s) * 100)

''' Runtime: 52 ms, faster than 37.26% of Python3 online submissions for Percentage of Letter in String.
Memory Usage: 13.8 MB, less than 97.26% of Python3 online submissions for Percentage of Letter in String. '''
