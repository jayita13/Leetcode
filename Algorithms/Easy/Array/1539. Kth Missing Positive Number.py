# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = []
        for i in range(1, max(arr)+k+1):
            if i not in arr:
                ans.append(i)
        return ans[k-1]
