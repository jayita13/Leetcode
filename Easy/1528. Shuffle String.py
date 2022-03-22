# https://leetcode.com/problems/shuffle-string/

 def restoreString(self, s: str, indices: List[int]) -> str:
 
        s1 = [''] * len(s) 
        
        for i in range(0,len(s1)):
            s1[indices[i]]=s[i]
            
        return ''.join(s1)

# Runtime: 73 ms, faster than 60.50% of Python3 online submissions for Shuffle String.
# Memory Usage: 13.8 MB, less than 70.46% of Python3 online submissions for Shuffle String.       
