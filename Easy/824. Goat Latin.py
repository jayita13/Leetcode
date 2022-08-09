# https://leetcode.com/problems/goat-latin/ 

class Solution:
    def toGoatLatin(self, sent: str) -> str:
        vow = "aeiouAEIOU"        
        ans = ""
        sent = sent.split()

        for i in range(len(sent)):
            if sent[i][0] in vow:
                ans += sent[i] + "ma" + "a"*(i+1) + " "
            else:
                ans += sent[i][1:] + sent[i][0] + "ma" + "a"*(i+1) + " "
                
        return ans.strip()
                    
""" Runtime: 47 ms, faster than 53.83% of Python3 online submissions for Goat Latin.
Memory Usage: 13.9 MB, less than 15.39% of Python3 online submissions for Goat Latin. """                    
