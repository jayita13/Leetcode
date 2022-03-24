# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        s1 = list(s)
        
        for i in range(1,len(s1),2):
            s1[i]= chr(ord(s1[i-1]) + int(s1[i]))  
            
        return "".join(s1)

# Runtime: 51 ms, faster than 33.50% of Python3 online submissions for Replace All Digits with Characters.
# Memory Usage: 13.9 MB, less than 22.50% of Python3 online submissions for Replace All Digits with Characters.
