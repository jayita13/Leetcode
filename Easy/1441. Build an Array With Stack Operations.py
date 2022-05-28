# https://leetcode.com/problems/build-an-array-with-stack-operations/ 

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        ans = []
        for i in range(1,max(target)+1):
            ans.append(i)
        for i in ans:            
            if i in target: 
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
        return res
                
''' Success Details 
Runtime: 52 ms, faster than 32.03% of Python3 online submissions for Build an Array With Stack Operations.
Memory Usage: 14 MB, less than 17.85% of Python3 online submissions for Build an Array With Stack Operations. '''                
