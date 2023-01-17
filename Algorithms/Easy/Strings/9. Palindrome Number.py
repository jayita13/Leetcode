# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False        

""" Runtime 62 ms Beats 81.47%
Memory 13.8 MB Beats 55.64% """
