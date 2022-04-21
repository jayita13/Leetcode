# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        num = []
        for i in range(n+1):
            num.append(sum(list(map(int,str(bin(i).replace("0b", ""))))))
        return num
