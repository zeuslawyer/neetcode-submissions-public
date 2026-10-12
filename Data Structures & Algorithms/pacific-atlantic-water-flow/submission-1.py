class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        self.atl, self.pac = set(), set()

        def climb(r, c, tracker, currHeight):
            # edge cases
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r, c) in tracker:
                return
            if heights[r][c] < currHeight:
                return

            tracker.add((r, c))
            # 4 directions
            climb(r + 1, c, tracker, heights[r][c])
            climb(r - 1, c, tracker, heights[r][c])
            climb(r, c + 1, tracker, heights[r][c])
            climb(r, c - 1, tracker, heights[r][c])

        # find all paths into pacific and atlantic
        for r in range(ROWS):
            climb(r, 0, self.pac, heights[r][0])
            climb(r, COLS - 1, self.atl, heights[r][COLS - 1])

        for c in range(COLS):
            climb(0, c, self.pac, heights[0][c])
            climb(ROWS - 1, c, self.atl, heights[ROWS-1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in self.pac and (r, c) in self.atl:
                    res.append([r, c])
        return res
