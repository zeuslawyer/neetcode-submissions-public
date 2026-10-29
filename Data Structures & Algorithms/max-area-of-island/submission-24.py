# DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        areas = []
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = [0]
                    self.dfs(r, c, grid, area, visited)
                    areas.append(area[0])

        return max(areas, default = 0)
    

    def dfs(self, r, c, grid, area, visited):
        if (r, c) in visited or grid[r][c] != 1: return
        visited.add((r,c))
        area[0]+=1

        if r-1 >= 0:
            self.dfs(r-1, c, grid, area, visited)
        if r+1 < len(grid):
            self.dfs(r+1, c, grid, area, visited)
        if c-1 >= 0:
            self.dfs(r, c-1, grid, area, visited)
        if c+1 < len(grid[0]):
            self.dfs(r, c+1, grid, area, visited)

    





