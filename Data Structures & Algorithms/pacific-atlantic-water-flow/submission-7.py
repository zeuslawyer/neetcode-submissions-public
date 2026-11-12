from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # visited nodes
        pacvisited, atlvisited = set(), set()

        # pac is row 0 and col0, atl is row n-1, col n-1
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    self.bfs(r,c, pacvisited, heights)
                
                if r == ROWS-1 or c == COLS-1:
                    self.bfs(r, c, atlvisited, heights)

        # iterate over grid. If (r,c) in BOTH sets then thats the answer
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacvisited and (r,c) in atlvisited:
                    res.append([r,c])
        

        return res
          

    def bfs(self, r,c, visited, heights):
        q = deque()
        q.append((r,c))
        visited.add((r,c))

        while q:
            row, col = q.popleft()
            for nr, nc in self.neighbours(row, col, heights):
                if (nr,nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
            

    def neighbours(self, r,c, heights):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr,dc, in directions:
            nr, nc = dr + r, dc + c
            if (
                nr >=0 and nr < len(heights) 
                and nc >= 0 and nc < len(heights[0])
                # since we are moving from waterline --> inland we want to ascend
                and heights[r][c] <= heights[nr][nc]
                ):
                yield nr, nc

    