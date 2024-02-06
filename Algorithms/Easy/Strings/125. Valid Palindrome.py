# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s1 = s.lower()
        st = ""
        for i in s1:
            if i.isalnum():
                st += i
        if st == st[::-1]:
            return True
        else:
            return False
        
""" Runtime
43
ms
Beats
76.07%
of users with Python3
Memory
17.10
MB
Beats
77.88%
of users with Python3 """        
