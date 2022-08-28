# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    def greatestLetter(self, s: str) -> str:
        unique = set()      
        maxi = ''
        for i in s:
            unique.add(i)
        for i in unique:
            if i.isupper():
                if i.lower() in unique:
                    maxi = max(maxi, i)

        return maxi
        
''' Runtime: 62 ms, faster than 53.88% of Python3 online submissions for Greatest English Letter in Upper and Lower Case.
Memory Usage: 13.8 MB, less than 70.62% of Python3 online submissions for Greatest English Letter in Upper and Lower Case. '''     
