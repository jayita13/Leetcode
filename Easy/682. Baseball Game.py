# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for i in ops:
            if i == 'C' :
                ans.pop()
            elif i == 'D':
                ans.append(int(ans[-1])*2)
            elif i == '+':
                ans.append(int(ans[-1])+int(ans[-2]))
            else:
                ans.append(int(i))
        return sum(ans)
        
''' Runtime: 36 ms, faster than 96.94% of Python3 online submissions for Baseball Game.
Memory Usage: 14.2 MB, less than 30.12% of Python3 online submissions for Baseball Game. '''        
