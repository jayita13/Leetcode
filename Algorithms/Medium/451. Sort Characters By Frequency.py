# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(k*v for k,v in Counter(s).most_common())
        
""" Runtime
35 ms
Beats
94.56%
Memory
15.2 MB
Beats
71.23% """        
