from collections import defaultdict
class Solution:    
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        # each row and col is key and its value is a set of numbers in that row or col
        rowsSet, colsSet = defaultdict(set), defaultdict(set)
        subgridSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # check if r,c is already in the row or col or subgrid
                val = board[r][c]
                if val == ".":
                    continue

                if (val in rowsSet[r] or
                    val in colsSet[c] or
                    val in subgridSet[(r//3, c//3)]
                ):
                    return False
                
                # update the collections with this valu
                rowsSet[r].add(val)
                colsSet[c].add(val)
                subgridSet[(r//3, c//3)].add(val)

        return True