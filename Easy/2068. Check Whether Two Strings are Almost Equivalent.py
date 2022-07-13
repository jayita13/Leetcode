# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        lst = list(set(word1) | set(word2))        
        for char in lst:
            if abs(word1.count(char) - word2.count(char)) > 3:
                return False
        return True

""" Success Details 
Runtime: 56 ms, faster than 39.00% of Python3 online submissions for Check Whether Two Strings are Almost Equivalent.
Memory Usage: 14 MB, less than 17.60% of Python3 online submissions for Check Whether Two Strings are Almost Equivalent. """
