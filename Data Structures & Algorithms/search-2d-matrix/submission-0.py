class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Intuition. Flatten the 2D array into a single array.
        Then binary search
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        lenArr = ROWS * COLS
        left, right = 0, lenArr - 1

        while left <= right:
            mid = (left + right) // 2
            valAtMid = self.idxToGridVal(mid, COLS, matrix)
            if target == valAtMid:
                return True
            
            if target < valAtMid:
                # target is on LHS
                right = mid - 1
            else:
                # value is on RHS
                left = mid + 1
        
        return False

    
    def idxToGridVal(self, idx, COLS, grid):
        r, c = idx//COLS, idx % COLS
        return grid[r][c]
        