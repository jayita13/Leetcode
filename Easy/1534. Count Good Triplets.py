# https://leetcode.com/problems/count-good-triplets/submissions/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j])<=a:
                    
                    for k in range(j+1, len(arr)):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            s+=1
        return s
        
'''Runtime 608ms
Memory  14MB'''
