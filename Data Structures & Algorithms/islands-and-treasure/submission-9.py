from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647 # land

        # enqueue all treasure cells in prep for BFS.
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                # start from Treasures
                if grid[r][c] == 0:
                    q.append((r, c))

        #BFS with cumulative accretion of distance
        while q:
            _r, _c = q.popleft()
            for nr, nc in self.getN(_r, _c, grid):
                # is land? then it is path of the path.
                # however its a neighbour, so its distance is 1+ the original popped cell, which may be >= 0 as it may have been enqueed at value > 0 (accretive)
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