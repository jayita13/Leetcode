# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = [s[0]]       
        for i in s[1:]:
            if res!=[] and i == res[-1]:
                res.pop(-1)
            else:
                res.append(i)
                
        return "".join(res)

''' Success Details 
Runtime: 102 ms, faster than 60.81% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 14.8 MB, less than 84.34% of Python3 online submissions for Remove All Adjacent Duplicates In String. '''
