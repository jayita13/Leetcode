# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        new_arr = sorted(arr)
        min_diff = new_arr[1] - new_arr[0]
        for i in range(len(new_arr)-1):
            if new_arr[i+1] - new_arr[i] < min_diff:
                min_diff = new_arr[i+1] - new_arr[i]
        for i in range(len(new_arr)-1):
            if new_arr[i+1] - new_arr[i] == min_diff:
                ans.append([new_arr[i],new_arr[i+1]])
        return ans
