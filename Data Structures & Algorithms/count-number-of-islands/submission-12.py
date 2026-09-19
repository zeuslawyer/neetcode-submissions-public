from collections import deque

class Solution:
    # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if not rows:
            return 0
            
        visited = []
        for i in range(rows):
            row = ["0"] * cols
            visited.append(row)
        
        islands = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and visited[i][j] != "1":
                    islands += 1
                    q = deque()
                    q.append((i,j))

                    while q:
                        r, c =  q.popleft()
                        visited[r][c] = "1"
                        neighbours = self.valid_neighbours(r,c,grid, visited)
                        for nr, nc in neighbours:
                            q.append((nr, nc))
                            visited[nr][nc] = "1"
        
        
        return islands
    
    
    def valid_neighbours(self, r,c,grid, visited):
        neighbours = []
        
        if r-1 >= 0 and visited[r-1][c] != "1" and grid[r-1][c] == "1":
            neighbours.append((r-1,c))
        if r+1 < len(grid) and visited[r+1][c] != "1" and grid[r+1][c] == "1":
            neighbours.append((r+1, c))
        
        if c-1 >= 0 and visited[r][c-1] != "1" and grid[r][c-1] == "1":
            neighbours.append((r, c-1))
        if c+1 < len(grid[0]) and visited[r][c+1] != "1" and grid[r][c+1] == "1":
            neighbours.append((r, c+1))
        
        return neighbours
    