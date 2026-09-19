class Solution:
    # DFS with self.area counter for mutability
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        if rows == 0:
            return maxArea
        
        visited = [[False]*cols for _ in range(rows)]


        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c >= cols or visited[r][c] or grid[r][c] == 0:
                return

            visited[r][c] = True
            self.area+=1

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.area =0
                    dfs(i,j)
                    maxArea = max(self.area, maxArea)

                

        return maxArea
