class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == 0 and cols == 0: return 0

        self.island_count = 0 
        self.visited = set()

        from collections import deque
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0" or (i, j) in self.visited: continue
                
                self.island_count +=1
                self.visited.add((i,j)) # add to visited on pop

                q = deque([(i, j)])
                while q:
                    curr = q.popleft()
                    self.visited.add((curr[0], curr[1]))

                    neighbours = self.get_neighbours(curr, grid)
                   
                    for nr, nc in neighbours:
                        if grid[nr][nc] == "0" or  (nr, nc) in self.visited: continue
                        q.append((nr,nc))
                        self.visited.add((nr, nc)) # add to visited on enqueue

        return self.island_count


    def get_neighbours(self, tup, grid):
        res = []
        r, c = tup

        if r-1 >=0:
            res.append((r-1, c))
            
        if r+1 < len(grid): 
            res.append((r+1, c))

        if c-1 >=0: 
            res.append((r, c-1))
        
        if c+1 < len(grid[0]): 
            res.append((r, c+1))

        return res





