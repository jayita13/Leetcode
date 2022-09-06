# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']        
        c,d = 0,0
        
        for i in a:
            if i in vowels:
                c+=1
        for i in b:
            if i in vowels:
                d+=1
        if c==d:
            return True
        else:
            return False

'''Runtime: 40 ms, faster than 81.10% of Python3 online submissions for Determine if String Halves Are Alike.
Memory Usage: 13.9 MB, less than 42.19% of Python3 online submissions for Determine if String Halves Are Alike.'''
