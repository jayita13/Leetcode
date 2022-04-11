# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = ""
        for i in range(len(s)//2):
            t = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = t
        

''' Runtime: 373 ms, faster than 12.01% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 89.63% of Python3 online submissions for Reverse String. '''
