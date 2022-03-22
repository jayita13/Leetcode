# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i+j==len(mat)-1:
                    s+= mat[i][j]
        return s

# Runtime: 237 ms, faster than 5.12% of Python3 online submissions for Matrix Diagonal Sum.
# Memory Usage: 14.1 MB, less than 61.44% of Python3 online submissions for Matrix Diagonal Sum.
