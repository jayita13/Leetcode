# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        row = []
        col = []
        res = []
        for i in mat:
            row.append(min(i))    

        new_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

        for i in new_mat:
            col.append(max(i))
        
        for i in row:
            if i in col:
                res.append(i)
        return res
        
''' Runtime: 134 ms, faster than 88.80% of Python3 online submissions for Lucky Numbers in a Matrix.
Memory Usage: 14.2 MB, less than 37.48% of Python3 online submissions for Lucky Numbers in a Matrix. '''        
