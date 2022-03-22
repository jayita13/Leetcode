# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

def cellsInRange(self, s: str) -> List[str]:
        row1 = int(s[1])
        row2 = int(s[4])
        col1 = ord(s[0]) 
        col2 = ord(s[3]) 
        res = []
        for i in range(col1, col2+1):  
            for j in range(row1, row2+1):
                res.append(f"{chr(i)}{j}") 
        return res

# Runtime: 70 ms, faster than 28.95% of Python3 online submissions for Cells in a Range on an Excel Sheet.
# Memory Usage: 13.9 MB, less than 72.63% of Python3 online submissions for Cells in a Range on an Excel Sheet.
