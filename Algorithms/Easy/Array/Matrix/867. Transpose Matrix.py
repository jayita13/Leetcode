# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        b = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                b[j][i] = matrix[i][j]

        return b
        
""" Runtime 74 ms Beats 72.35%
Memory 14.7 MB Beats 49.55% """  
