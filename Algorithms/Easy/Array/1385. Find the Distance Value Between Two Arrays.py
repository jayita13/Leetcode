# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        for i in arr1:
            f=0
            for j in sorted(arr2):
                if abs(i-j) <= d:
                    f = 1
                    break
            if f==0:
                c+=1
                
        return c
        
