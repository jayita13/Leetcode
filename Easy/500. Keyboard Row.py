# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        
        for word in words:
            if all(ch in row1 for ch in word.lower()) or all(ch in row2 for ch in word.lower()) or all(ch in row3 for ch in word.lower()):
                ans.append(word)
                
""" Success Details 
Runtime: 43 ms, faster than 58.76% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.8 MB, less than 97.74% of Python3 online submissions for Keyboard Row. """                
