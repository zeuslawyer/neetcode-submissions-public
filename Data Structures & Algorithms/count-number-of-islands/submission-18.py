from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])

        if rows == 0:
            return 0
        
        islands = 0

        visited = [[False]* cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    # visited[i][j] = True
                    self.bfs(i,j, grid, visited)

        return islands


    def bfs(self, r, c, grid, visited):
        q = deque([(r, c)])

        while q:
            r,c = q.popleft()
            # visited[r][c] = True
            neighbours = self.valid_neighbours(r, c, grid, visited)
            for nr, nc in neighbours:
                visited[nr][nc] = True
                q.append((nr, nc))
    
    def valid_neighbours(self, r, c, grid,visited):
        neighbours = []

        if r-1 >= 0 and grid[r-1][c] == "1" and not visited[r-1][c]:
            neighbours.append((r-1, c))

        if r+1 < len(grid) and grid[r+1][c] == "1" and not visited[r+1][c]:
            neighbours.append((r+1, c))

        if c-1 >= 0 and grid[r][c-1] == "1" and not visited[r][c-1]:
            neighbours.append((r, c-1))

        if c+1 < len(grid[0]) and grid[r][c+1] == "1" and not visited[r][c+1]:
            neighbours.append((r, c+1))
        
        return neighbours


