# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subs = set()
        i=0
        for i,j in enumerate(words):
            for k in words[:i]:
                if j in k:
                    subs.add(j)
            for l in words[i+1:]:
                if j in l:
                    subs.add(j)
            i+=1
            
        return subs
        
""" Runtime: 45 ms, faster than 83.78% of Python3 online submissions for String Matching in an Array.
Memory Usage: 13.9 MB, less than 64.11% of Python3 online submissions for String Matching in an Array. """        
