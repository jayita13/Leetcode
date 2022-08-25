# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, s1: str, s2: str) -> bool:
        
        for i in s1:
            if s2.count(i) < s1.count(i):
                return False
        return True
    
        # return not Counter(ransomNote) - Counter(magazine)
        
""" Runtime: 250 ms, faster than 5.00% of Python3 online submissions for Ransom Note.
Memory Usage: 14.2 MB, less than 53.79% of Python3 online submissions for Ransom Note. """        
