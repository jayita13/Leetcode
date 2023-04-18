# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i,j in zip(word1, word2):
            merged.append(i)      
            word1 = word1.replace(i,"",1)
            merged.append(j)
            word2 = word2.replace(j,"",1)
        
        merged.append(word1)
        merged.append(word2)

        return "".join(merged)
    
    """
    s = ""
        for i,j in zip(w1, w2):
            s += i
            s += j
            w1 = w1.replace(i,"",1)
            w2 = w2.replace(j,"",1)
        return s+w1+w2
    """

''' Runtime: 32 ms, faster than 88.16% of Python3 online submissions for Merge Strings Alternately.
Memory Usage: 13.9 MB, less than 19.56% of Python3 online submissions for Merge Strings Alternately. '''

""" Runtime
24 ms
Beats
96.72%
Memory
13.8 MB
Beats
55.13% """
