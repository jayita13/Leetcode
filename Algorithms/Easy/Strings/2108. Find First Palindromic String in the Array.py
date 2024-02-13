# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # s=""
        # for word in words:
        #     if word  == "".join(reversed(word)):
        #         s = word
        #         break  
        # return s

        for word in words:
            if word == word[::-1]:
                return word
            
        return ""

# Runtime: 124 ms, faster than 37.62% of Python3 online submissions for Find First Palindromic String in the Array.
# Memory Usage: 13.8 MB, less than 97.19% of Python3 online submissions for Find First Palindromic String in the Array.
