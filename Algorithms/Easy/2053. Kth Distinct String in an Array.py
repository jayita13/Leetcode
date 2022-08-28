# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = []
        ans = ""
        for i in arr:
            if arr.count(i) == 1:
                seen.append(i)
        for i in range(len(seen)):
            if i+1 == k:
                ans = seen[i]
        return ans

