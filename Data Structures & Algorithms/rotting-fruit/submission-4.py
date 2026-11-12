from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # enqueue all the rotten oranges as they radiate rot around them
        # count fresh fruit so we can see if there are 0 left later
        freshcount = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshcount += 1


        minutes = 0
        while q and freshcount > 0:
            # we need level order traversal as the radiation happens in all directions, to all neighbours in the same minute
            qlen = len(q)
            minutes += 1
            for i in range(qlen):
                rotr, rotc = q.popleft()
                for fr, fc in self.neighbours(rotr, rotc, grid):
                    if grid[fr][fc] == 1:  # only fresh fruit are made rotten
                        grid[fr][fc] = 2 # mark fresh as rotten
                        freshcount -= 1
                        q.append((fr, fc))

        return minutes if freshcount == 0 else -1
        
    def neighbours(self,  r, c, grid):
        directions = [(1, 0), (-1, 0), (0,1), (0,-1)]

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc

