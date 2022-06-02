# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        seen = list(words[0])
        for i in words:
            res = []
            for j in i:
                if j in seen:
                    res.append(j)
                    seen.remove(j)
            seen = res
        return seen
        
''' Runtime: 53 ms, faster than 83.76% of Python3 online submissions for Find Common Characters.
Memory Usage: 13.9 MB, less than 96.19% of Python3 online submissions for Find Common Characters. '''      

