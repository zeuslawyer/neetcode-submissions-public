from collections import deque

#BFS 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        areas=[]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q = deque()
                    q.append((r, c))
                    visited.add((r,c))
                    area = 0

                    while q:
                        qr, qc = q.popleft()
                        area +=1
                        for nr, nc in self.neighbours(qr, qc, grid):
                            if ((nr, nc)) not in visited and grid[nr][nc] == 1:
                                visited.add((nr, nc))
                                q.append((nr,nc))

                    areas.append(area)
        
        return max(areas, default=0)


    def neighbours(self, r,c, grid):
        directions = [(1, 0), (-1, 0), (0,1), (0, -1)]

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc
        