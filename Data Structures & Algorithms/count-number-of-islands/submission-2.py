class Solution:
    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
    
        islands = 0
        rows, cols = len(grid), len(grid[0])

        visited = [] 
        for i in range(rows):
            row = ["0"] * cols
            visited.append(row)
        
        
        def dfs(r, c):            
            if r< 0 or r >= rows or c < 0 or c >= cols:
                return

            if visited[r][c] == "1" or grid[r][c] != "1":
                return
            
            visited[r][c]= "1"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] != "1":
                    islands +=1

                    dfs(i,j)

        
        return islands




        
        
        

            



            
            

            

        