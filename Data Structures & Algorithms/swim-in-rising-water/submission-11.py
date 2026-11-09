class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
            # elevation must be <= water height t for us to swimInWater
        # therefore, for any path from start to end, the amount of time
        # is determined/constrained by the highest height on the path. That is
        # the MINIMUM value that T will need to be.
        # If we treat heights as a weight/distance, then we can apply a min heap to track the path with the lowest height in the grid.
        # we pop the paths with the min heights until we find the END point.

        timeTo = {}

        minheap = [(grid[0][0], 0, 0)] # time, r, c
        heapq.heapify(minheap)

        maxheight = 0 # max height along the path will produce the min time.
        while minheap:
            t, r, c = heapq.heappop(minheap)
            if not (r,c) in timeTo:
                timeTo[(r,c)] = t
                maxheight = t

                # exit condition
                if r == len(grid)-1 and c == len(grid[0]) - 1:
                    return maxheight

                # process neighbours and retain max height.
                for nt, nr, nc in self.getNeighbours(r, c, grid):
                    # retain the maxheight see on this path so far. Do NOT accumulate heights.
                    maxh = max(nt, maxheight)
                    heapq.heappush(minheap, (maxh, nr, nc))
        
        return maxheight

    def getNeighbours(self, r, c, grid):
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

        for dr, dc in directions:
            nr, nc = dr+r, dc + c
            if nr >=0 and nr < len(grid) and nc >=0 and nc < len(grid[0]):
                yield grid[nr][nc], nr, nc

    
