from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
            # BFS only from edges in to disqualify edge-connected regions
                if i > 0 and i < ROWS - 1 and j > 0 and j < COLS - 1:
                    continue
                
                # we only want border cells with 'O'
                if board[i][j] == "O":
                    q =  deque()
                    q.append((i,j))
                    board[i][j] = "#" # disqualify cell

                    while q:
                        r, c = q.popleft()
                        for nr, nc in self.neighbours(r,c, board):
                            if board[nr][nc] == 'O':
                                board[nr][nc] = "#"
                                q.append((nr, nc))
                    

        # capture the Os by flipping to X and reset the disqualified cells from #
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                if board[i][j] == "#":
                    board[i][j] = "O"

    def neighbours(self, r, c, board):
        directions = [(-1, 0), (1,0), (0,-1), (0, 1)] 
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                yield nr, nc


        