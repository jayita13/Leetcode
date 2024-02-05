# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        p = []
        for i,j in enumerate(words):
            if x in j:
                p.append(i)
        return p

""" Runtime 44 ms Beats 99.82% of users with Python3 
Memory 16.59 MB Beats 66.93% of users with Python3 """
