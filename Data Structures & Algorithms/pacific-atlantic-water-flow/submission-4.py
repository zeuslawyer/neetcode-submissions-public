# BFS
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find all paths from the oceans inwards
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        # Originating in pacific
        pacq = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0):
                    pacq.append((r,c))
                    pac.add((r,c))
        
        # Originating in atlantic
        atlq = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS-1 or c == COLS-1:
                    atlq.append((r,c))
                    atl.add((r,c))

        # process both queues
        self.bfs(pacq, pac, heights)
        self.bfs(atlq, atl, heights)

        res = [] 
        for i in range(ROWS):
            for j in range (COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res


    def bfs(self, q, visited, heights):
        while q:
            r,c = q.popleft()
            visited.add((r,c))
            for nr, nc in self.neighbours(r,c,heights):
                if heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
    
    
    def neighbours(self, r, c, heights):
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0),(1, 0), (0,-1), (0, 1)]
        
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                yield nr, nc
