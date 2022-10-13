# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        dict_ = {}
        
        for i in range(len(names)):
            dict_[heights[i]] = names[i] 
            
        for i in sorted(dict_.keys()):
            arr.append(dict_[i])
            
        return arr[::-1]
     
""" Success Details 
Runtime: 218 ms, faster than 71.46% of Python3 online submissions for Sort the People.
Memory Usage: 14.5 MB, less than 11.01% of Python3 online submissions for Sort the People. """
