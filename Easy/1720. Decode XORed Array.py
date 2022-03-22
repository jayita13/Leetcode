# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            ans.append(ans[-1]^i)
        return ans

# Runtime: 327 ms
# Memory Usage: 15.8 MB    
