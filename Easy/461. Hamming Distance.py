# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x).replace("0b", "")
        bin_y = bin(y).replace("0b", "")
        
        if len(bin_x)-len(bin_y)>0:             
            bin_y='0'*(len(bin_x)-len(bin_y))+str(bin_y)
        if len(bin_y)-len(bin_x)>0:
            bin_x='0'*(len(bin_y)-len(bin_x))+str(bin_x)
        
        c = 0
        
        for i, j in zip(list(map(int, str(bin_x))), list(map(int, str(bin_y)))):
            if i!=j:
                c+=1
        return c
      
''' Runtime: 54 ms, faster than 20.45% of Python3 online submissions for Hamming Distance.
Memory Usage: 13.8 MB, less than 63.62% of Python3 online submissions for Hamming Distance. ''' 
