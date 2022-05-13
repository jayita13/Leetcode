# https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for i in words:
            if s.startswith(i):
                c+=1
        return c
        
''' Runtime: 72 ms, faster than 63.05% of Python3 online submissions for Count Prefixes of a Given String.
Memory Usage: 14.1 MB, less than 46.81% of Python3 online submissions for Count Prefixes of a Given String. '''        
