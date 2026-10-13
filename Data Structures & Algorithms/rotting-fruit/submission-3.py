from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        freshcount = 0


        # Add rottens to q. Count fresh oranges.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append((r,c))
                if grid[r][c] == FRESH:
                    freshcount+=1

        minutes = 0
        # BFS level order as 1 level deeper => +1m elapsed.
        # only BFS while there are still fresh fruit
        while q and freshcount > 0 :
            for i in range(len(q)):
                r,c = q.popleft()
                neighbours = self.getFreshNeighbours((r,c), grid)

                for nr, nc in neighbours:
                    grid[nr][nc] = ROTTEN
                    freshcount -=1
                    q.append((nr, nc))
            
            minutes+=1

        # if there are still fresh fruit left then -1
        return minutes if freshcount == 0 else -1


    def getFreshNeighbours(self, node, grid):
        r,c = node

        res = []
        if r > 0 and grid[r-1][c] == 1:
            res.append([r-1, c])
        if r < len(grid)-1 and grid[r+1][c] == 1:
            res.append([r+1, c])
        if c >0 and grid[r][c-1] ==1:
            res.append([r, c-1])
        if c < len(grid[0])-1 and grid[r][c+1] == 1:
            res.append([r, c+1])
        
        return res



