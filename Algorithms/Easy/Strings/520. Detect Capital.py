# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower() or word == word.capitalize():
            return True
        else:
            return False
         
""" Runtime 54 ms """
