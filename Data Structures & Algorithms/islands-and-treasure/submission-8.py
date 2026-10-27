from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        # enqueue all treasure cells in prep for BFS.
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        #BFS 
        while q:
            _r, _c = q.popleft()
            for nr, nc in self.getN(_r, _c, grid):
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[_r][_c] + 1
                    q.append((nr, nc))

    def getN(self, r, c, grid):
        """
        excludes water (-1) cells
        """
        res = []
        if r-1 >= 0 and grid[r-1][c] != -1:
            res.append([r-1, c])
        if r+1 < len(grid) and grid[r+1][c] != -1:
            res.append([r+1, c])
        if c-1 >= 0 and grid[r][c-1] != -1:
            res.append([r, c-1])
        if c+1 < len(grid[0]) and grid[r][c+1] != -1:
            res.append([r, c+1])
        return res