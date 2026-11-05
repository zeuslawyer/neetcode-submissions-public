import collections
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])

        def coordToIdx(r,c):
            interim = r * COLS + c 
            return (k + interim) % (ROWS * COLS)
        
        def idxToCoord(idx):
            return(idx // COLS, idx % COLS) # r, c

        res = [ [0] * COLS for i in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]
                # Flatten into NOTIONAL 1D index for r, c
                idx = coordToIdx(r, c)
                # find 2D index and offset by k for insertion into new grid
                targr, targc = idxToCoord(idx)

                res[targr][targc] = val

        return res

