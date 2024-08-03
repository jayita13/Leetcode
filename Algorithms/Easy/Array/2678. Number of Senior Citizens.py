# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        s = 0 
        for i in details:
            if int(i[11:13]) > 60:
                s += 1
        return s

""" Runtime 39ms Beats 92.71% 
Memory 16.57MB Beats 39.13% """
