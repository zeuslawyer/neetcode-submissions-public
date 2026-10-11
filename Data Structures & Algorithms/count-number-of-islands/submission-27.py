class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == 0 or cols == 0 : return 0

        self.island_count = 0
        self.visited =  set()
        for i in range(rows):
            for j in range(cols):
                if (i, j) in self.visited or grid[i][j] == "0": 
                    continue
                
                self.island_count += 1
                self.dfs((i,j), grid)

        return self.island_count


    def dfs(self, node, grid):
        r, c = node
        if (r,c) in self.visited or grid[r][c] == "0":
            return
        
        self.visited.add((r,c))
        if r-1 >=0 : self.dfs((r-1, c), grid)
        if r+1 < len(grid) : self.dfs((r+1, c), grid)

        if c-1 >= 0 : self.dfs((r, c-1), grid)
        if c+1 < len(grid[0]): self.dfs((r, c+1), grid)
