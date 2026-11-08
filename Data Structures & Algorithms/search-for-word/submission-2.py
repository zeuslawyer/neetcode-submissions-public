# INTUITION: DFS + Backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            # base conditions
            if i == len(word): return True # word found
            if (r,c) in visited: return False
            if (r<0 or r>=ROWS or c < 0 or c >=COLS): return False
            if board[r][c] != word[i] : return False

            visited.add((r,c))

            # dfs on all neighbours.
            # since we need to backtrack later we store the bool results
            found =  (
                dfs(r+1, c, i+1) 
                or dfs(r-1, c, i+1) 
                or dfs(r, c + 1, i+1)
                or dfs(r, c -1 , i+1) 
            )

            visited.remove((r,c))

            return found

        # navigate the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False