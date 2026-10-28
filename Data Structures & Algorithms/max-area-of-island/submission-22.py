from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        areas = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    q = deque()
                    q.append((r, c))
                    visited.add((r,c))
                    area = 0
                    
                    while q:
                        row, col = q.popleft()
                        area += 1
                        for nei in self.neighbours(row, col, grid):
                            if nei not in visited:
                                q.append(nei)
                                visited.add(nei)

                    areas.append(area)

        return max(areas, default=0)


    def neighbours(self, row, col, grid):
        res = []
        if row > 0 and grid[row-1][col] == 1: res.append((row-1, col))
        if col >0 and grid[row][col-1] == 1 : res.append((row, col-1))
        if row < len(grid)-1 and grid[row+1][col] == 1 : res.append((row+1, col))
        if col < len(grid[0])-1 and grid[row][col+1] == 1: res.append((row, col+1))

        return res