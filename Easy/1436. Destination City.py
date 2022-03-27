# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = []
        dest = []
        
        for i in range(len(paths)):
            src.append(paths[i][0])
            dest.append(paths[i][1])
        
        for i in dest:
            if i not in src:
                return i     
              
''' Runtime: 65 ms, faster than 70.90% of Python3 online submissions for Destination City.
Memory Usage: 13.9 MB, less than 47.46% of Python3 online submissions for Destination City. '''
