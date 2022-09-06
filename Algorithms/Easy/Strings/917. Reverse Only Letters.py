# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = []
        letters = []
        for i in s:
            if i.isalpha():
                letters.append(i)
        for i in s:
            if i.isalpha():
                res.append(letters.pop())
            else:
                res.append(i)
        return "".join(res)
        
""" Runtime: 52 ms, faster than 38.62% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 14 MB, less than 16.57% of Python3 online submissions for Reverse Only Letters. """        
