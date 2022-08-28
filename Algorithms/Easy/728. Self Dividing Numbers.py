# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_div(n):
            if "0" not in str(n) and all(n % int(letter)==0 for letter in str(n)):
                return True
            return False
                
            
        ans = []
        for i in range(left,right+1):
            if self_div(i):
                ans.append(i)
        
        return ans

''' Runtime: 110 ms, faster than 15.49% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 13.8 MB, less than 98.26% of Python3 online submissions for Self Dividing Numbers. '''
