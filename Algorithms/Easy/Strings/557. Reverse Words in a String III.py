# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        new = s.split()
        s1=[]
        for i in new:
            s1.append(i[::-1])
        
        return " ".join(s1)

'''Runtime: 57 ms, faster than 56.67% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.8 MB, less than 20.43% of Python3 online submissions for Reverse Words in a String III.'''
