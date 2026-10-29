from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # multi bfs.  start with all the regions with O starting from the edges
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                   q.append((r,c)) 

        while q:
            r,c = q.popleft()
            board[r][c] = "#"
            for nr, nc in self.neighbours(r,c, board):
                if board[nr][nc] == "O":
                    q.append((nr, nc))
                    board[nr][nc] = "#"
        
        # iterate over the grid to capture remaining "O"s and reset "#"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "#":
                    board[r][c] = "O"
            

    def neighbours(self, r, c, board):
        dirs = [(-1,0),(1, 0), (0,-1), (0,1)]
        ROWS = len(board)
        COLS = len(board[0])

        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                yield nr, nc
    

        
        


