# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def cal(word):
            s = ""
            for w in word:
                s += str(ord(w)-97)
            s = s.lstrip("0")
            if s == "":
                return 0
            else:
                return int(s)
        if cal(firstWord) + cal(secondWord) == cal(targetWord):
            return True
        else:
            return False
            
""" Runtime 35 ms Beats 42.81%
Memory 13.9 MB Beats 12.60%   """  
