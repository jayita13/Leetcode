# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for i in range(len(gain)):
            alt.append(alt[-1]+gain[i])
        return max(alt)

# Runtime: 62 ms, faster than 22.27% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 13.9 MB, less than 61.72% of Python3 online submissions for Find the Highest Altitude.
