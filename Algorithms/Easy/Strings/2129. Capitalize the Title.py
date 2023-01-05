# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        str = ""
        for i in title.split():
            if len(i) == 1 or len(i) == 2:
                str += i.lower() + " "
            else:
                str += i.capitalize() + " "
                
        return str.rstrip()

""" Runtime 81 ms """
