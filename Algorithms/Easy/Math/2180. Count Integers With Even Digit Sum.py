# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        ss = 0
        for i in range(1,num+1):
            s=0
            while i>0:
                s+=i%10
                i//=10
            if s%2==0:
                ss+=1
            
        return ss
        
""" Runtime: 67 ms, faster than 48.57% of Python3 online submissions for Count Integers With Even Digit Sum.
Memory Usage: 13.9 MB, less than 11.57% of Python3 online submissions for Count Integers With Even Digit Sum. """        
