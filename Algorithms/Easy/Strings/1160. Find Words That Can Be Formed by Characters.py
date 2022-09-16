# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0
        for i in words:
            for j in i:
                if i.count(j) > chars.count(j):
                    break
            else:
                s += len(i)
        return s

""" Runtime: 193 ms, faster than 74.16% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.6 MB, less than 37.58% of Python3 online submissions for Find Words That Can Be Formed by Characters. """
