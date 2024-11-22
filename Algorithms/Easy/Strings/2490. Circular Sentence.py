# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        for i in range(len(s)):
            if s[i-1][-1] != s[i][0]:
                return False
        return True

""" Runtime 0 ms Beats 100.00%
Memory 16.61 MB Beats 19.74% """
