# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            s1 = word[:word.index(ch)+1]
            s2 = word[word.index(ch)+1:]
            return s1[::-1]+s2                
      
''' Runtime: 28 ms, faster than 95.21% of Python3 online submissions for Reverse Prefix of Word.
Memory Usage: 13.9 MB, less than 20.01% of Python3 online submissions for Reverse Prefix of Word. '''
