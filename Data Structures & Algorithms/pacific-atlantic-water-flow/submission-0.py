# DFS
class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights),   len(heights[0])

        self.reachablePac, self.reachableAtl = set(), set()

        # recursively climb and find path 
        def climb(r, c, trackerset, prevHeight):
            if (r,c) in trackerset: return
            if r < 0 or r == ROWS or c <0 or c == COLS: return
            # access heights last after validating r and c in bounds.
            if heights[r][c] < prevHeight: return 

            trackerset.add((r,c))
            prevHeight = heights[r][c]

            # 4 directions
            climb(r-1, c, trackerset, prevHeight)
            climb(r+1, c, trackerset, prevHeight)
            climb(r, c-1, trackerset, prevHeight)
            climb(r, c+1, trackerset, prevHeight)


        # navigate from water inwards - iterating over rows -> firt and last cols have mouths
        for r in range(ROWS):
            # 0th col = Pacific
            climb(r, 0, self.reachablePac,heights[r][0])
            # Last col = Atlantic
            climb(r, COLS-1, self.reachableAtl, heights[r][COLS-1])

        # navigate from water inwards - iterative over cols, first and last rows have mouths
        for c in range(COLS):
            # 0th row -> Pacific
            climb(0, c, self.reachablePac, heights[0][c])
            # Last row -> Atlantic
            climb(ROWS-1, c, self.reachableAtl, heights[ROWS-1][c])


        # VIsit each cell to see if present in both trackerset
        res = [] 
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in self.reachablePac and (r,c) in self.reachableAtl:
                    res.append([r,c])
        
        return res
          


        

