# https://leetcode.com/problems/is-subsequence
 
import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        return re.search(".*".join(list(s)),t)      
# This line joins the characters of the s string with the string ".*" in between each character. 
# This effectively creates a regular expression pattern that matches any characters in t in the order specified by the characters in s. 
# For example, if s is "abc," then this expression becomes "a.*b.*c."

""" Runtime Details
1663ms Beats 5.52%of users with Python3
Memory Details
16.15MB Beats 98.29%of users with Python3 """
