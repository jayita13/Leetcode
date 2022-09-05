 # https://leetcode.com/problems/three-consecutive-odds/
 
 class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
        return False

""" Runtime: 102 ms, faster than 7.07% of Python3 online submissions for Three Consecutive Odds.
Memory Usage: 14.1 MB, less than 18.26% of Python3 online submissions for Three Consecutive Odds. """
