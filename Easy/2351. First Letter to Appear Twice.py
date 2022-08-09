# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = set()
        f = ''
        for i in s:
            if i in l:
                f = i
                break
            else:
                l.add(i)
        return f
            
""" Runtime: 43 ms, faster than 64.79% of Python3 online submissions for First Letter to Appear Twice.
Memory Usage: 13.9 MB, less than 51.74% of Python3 online submissions for First Letter to Appear Twice. """            
