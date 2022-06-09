# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(10,27):
            s=s.replace(str(i)+'#',chr(96+i))
        for i in range(1,10):
            s=s.replace(str(i),chr(96+i))
        return s

''' Runtime: 46 ms, faster than 43.60% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
Memory Usage: 13.8 MB, less than 66.99% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping. '''
