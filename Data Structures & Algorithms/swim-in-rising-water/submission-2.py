# Modified Dijskra
# Since water level must be > elevation, the higher the elevation the more time.
# we are looking for min time ==> path with the least elevations.

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        startElev = grid[0][0]
        visited = set()
        minheap =[(startElev, 0, 0)] # starting r, c as well
        heapq.heapify(minheap)

        while minheap:
            # we track the max elevation at a given path. 
            # the minheap will give us the minimum max elevations.
            elev, row, col = heapq.heappop(minheap)

            if row == ROWS-1 and col == COLS-1:
                    return elev

            if (elev, row, col) not in visited:
                visited.add((elev, row, col))

                for nr, nc in self.neighbours(row, col, grid):
                    # find the max height so far, and push onto heap
                    height = grid[nr][nc]
                    maxElev = max(height, elev)
                    heapq.heappush(minheap, (maxElev, nr, nc))
        
    def neighbours(self, r, c, grid):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc


