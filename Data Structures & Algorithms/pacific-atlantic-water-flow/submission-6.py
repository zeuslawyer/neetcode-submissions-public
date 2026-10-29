# DFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # traverse pacific edges and climb up
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    self.climb(r, c, pac, heights, heights[r][c])

        # traverse atlantic edges and climb up
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS-1 or c == COLS-1:
                    self.climb(r, c, atl, heights, heights[r][c])    
        

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res
    
    def climb(self, r, c, visited, grid, prevHeight):
        if (r, c) in visited: return
        
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return

        if grid[r][c] < prevHeight: return 

        visited.add((r,c))
        currHeight = grid[r][c]

        self.climb(r-1, c, visited, grid,currHeight )
        self.climb(r+1, c, visited, grid, currHeight)
        self.climb(r, c-1, visited, grid, currHeight)
        self.climb(r, c + 1, visited, grid, currHeight)