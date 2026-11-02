import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # elevation must be <= water height t for us to swimInWater
        # therefore, for any path from start to end, the amount of time
        # is determined/constrained by the highest height on the path. That is
        # the MINIMUM value that T will need to be.
        # If we treat heights as a weight/distance, then we can apply a min heap to track the path with the lowest height in the grid.
        # we pop the paths with the min heights until we find the END point.

        minheap = [(grid[0][0], 0, 0)] # max height so far, starting r and c
        heapq.heapify(minheap)
        visited = set()

        while minheap:
            h, r, c = heapq.heappop(minheap)

            if r == len(grid)-1 and c == len(grid[0]) - 1:
                return h

            if (r,c) not in visited:
                visited.add((r,c))
                
                for nr, nc in self.neighbours(r,c, grid):
                     # track max height so far
                    maxHeight = max(h, grid[nr][nc])
                    heapq.heappush(minheap, (maxHeight, nr, nc))

    def neighbours(self, r, c, grid):
        directions = [(1, 0), (-1,0), (0,1), (0,-1)]    
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc





