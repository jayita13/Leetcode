# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = -1
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                f = i
                break
                
        return f

        # alt sol
        # ans = -1
        # for i,j in enumerate(s):
        #     if j not in s[i+1:] and j not in s[:i]:
        #         ans = i
        #         break
        # return ans

        
