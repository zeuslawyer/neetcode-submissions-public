class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        if rows == 0:
            return maxArea
        
        visited = [[False]*cols for _ in range(rows)]


        def dfs(r, c, island=[]):
            if r<0 or c<0 or r>=rows or c >= cols or visited[r][c] or grid[r][c] == 0:
                return

            visited[r][c] = True
            island.append(1)

            dfs(r-1, c, island)
            dfs(r+1, c, island)
            dfs(r, c-1, island)
            dfs(r, c+1, island)

            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    island = []
                    dfs(i,j, island)
                    maxArea = max(len(island), maxArea)

                

        return maxArea
