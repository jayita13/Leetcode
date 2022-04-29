# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(arr)==1 and arr[0] == target[0]:
            return True
        f = 0 
        for i in arr:
            if i not in target:
                f=1  
                break
        if f == 0:
            c=0
            for i,j in zip(sorted(arr),sorted(target)):
                if i != j:
                    c = 1
                    break
        else:
            return False
        
        if c == 0:
            return True
        else:
            return False
