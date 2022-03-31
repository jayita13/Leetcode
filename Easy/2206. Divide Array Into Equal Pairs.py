# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = {}
        f=0
        for i in nums:
            res[i] = res.get(i, 0) + 1
        for i in res.values():
            if i%2!=0:
                f=1
                break
        if f==1:
            return False
        else:
            return True
            
''' Runtime: 97 ms, faster than 84.43% of Python3 online submissions for Divide Array Into Equal Pairs.
Memory Usage: 14.1 MB, less than 66.92% of Python3 online submissions for Divide Array Into Equal Pairs. '''           
