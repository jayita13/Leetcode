# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c = 0
        for i in patterns:
            if i in word:
                c+=1
                
        return c

''' Runtime: 42 ms, faster than 72.42% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
Memory Usage: 13.9 MB, less than 80.90% of Python3 online submissions for Number of Strings That Appear as Substrings in Word. '''
