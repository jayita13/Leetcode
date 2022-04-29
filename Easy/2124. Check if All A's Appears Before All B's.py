# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        a = []
        b = []
        for i in range(len(s)):
            if s[i] == 'a':
                a.append(i)
            else:
                b.append(i)
        c=0
        if len(a) == 0:
            return True
        for idx in a:
            for ind in b:
                if idx > ind:
                    c = 1
                    break
        if c == 0:
            return True
        else:
            return False
                        
      
