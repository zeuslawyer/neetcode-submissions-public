from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF=2147483647

        q = deque() # fill with coordinate tups

        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == 0: # 0 is also the starting distance of chest to itself.
                    q.append((r, c))
        

        # BFS over q
        while q:
            pr, pc = q.popleft()

            for nr, nc in self.neighbours(pr,pc, grid):
                if grid[nr][nc] == INF: # this is effectively "unvisited" check
                    grid[nr][nc] = 1 + grid[pr][pc] # child is 1 + number in parent cell
                    q.append((nr, nc))
            

    def neighbours(self, r, c, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if (0<= nr < len(grid) and 0 <= nc < len(grid[0])):
                yield nr, nc


