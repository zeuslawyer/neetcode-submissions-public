from collections import deque
class Solution:
    # BFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if rows == 0:
            return 0
        
        area = 0 

        visited = [[False] * cols for i in range(rows)]

        def bfs(r,c):
            q = deque()
            if not visited[r][c] and grid[r][c] == 1:                
                q.append((r,c))
                self.count +=1

            while q:
                _r, _c = q.popleft()
                visited[_r][_c] = True
                neighbours = valid_neighbours(_r, _c)
                for nr, nc in neighbours:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    self.count+=1

            

        def valid_neighbours(r, c):
            neighbours = []

            if r-1 >= 0 and grid[r-1][c] != 0 and not visited[r-1][c]:
                neighbours.append((r-1, c))

            if r+1 < len(grid) and grid[r+1][c] != 0 and not visited[r+1][c]:
                neighbours.append((r+1, c))
                
            if c-1 >= 0 and grid[r][c-1] != 0 and not visited[r][c-1]:
                neighbours.append((r, c-1))

            if c+1 < len(grid[0]) and grid[r][c+1] != 0 and not visited[r][c+1]:
                neighbours.append((r, c+1))

            return neighbours
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1 or visited[i][j]:
                    continue
                else: 
                    self.count = 0
                    bfs(i,j)
                    area = max(area, self.count)
        
        return area