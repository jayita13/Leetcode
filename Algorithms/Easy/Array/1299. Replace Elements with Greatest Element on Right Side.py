# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
            return arr
        
        for i in range(len(arr)-1):
            if i==len(arr)-1:
                arr[i] = arr[len(arr)-1]                
            else:
                arr[i] = max(arr[i+1:])
                
        arr[-1] = -1
        return arr

