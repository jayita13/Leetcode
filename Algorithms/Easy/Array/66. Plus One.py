# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        s = ""
        for i in digits:
            s += str(i)
        n = int(s) + 1
        return list(map(int, str(n)))
        
""" Runtime
38 ms
Beats
31.53%
Memory
13.8 MB
Beats
92.70% """        
