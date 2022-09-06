# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        c = 0
        while True:
            if num1==0 or num2==0:
                break            
            elif num1 >= num2:
                num1-=num2   
            elif num2 > num1:
                num2-=num1
            c+=1
            
        return c

'''Runtime: 152 ms, faster than 50.81% of Python3 online submissions for Count Operations to Obtain Zero.
Memory Usage: 13.8 MB, less than 66.55% of Python3 online submissions for Count Operations to Obtain Zero.'''
