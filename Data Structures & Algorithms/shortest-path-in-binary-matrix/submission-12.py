from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1: return -1
        
        count = 0
        visited = set()
        visited.add((0,0))
    
        q = deque([(0,0)])

        while q:
            # level order as each level is 1 step in count
            for i in range(len(q)):
                r,c = q.popleft()
                if r == ROWS-1 and c == COLS -1:
                    count +=1
                    return count
                # get neighbours
                neighbours = self.neighboursOf((r,c))
                for nr, nc in neighbours:
                    if nr < 0 or nr > ROWS-1 or nc < 0 or nc > COLS-1:
                        continue
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr,nc))

            count+=1   
        
        return -1


    def neighboursOf(self, node):
        r,c = node
        return [(r-1, c),(r+1, c), (r, c-1),(r, c+1),(r-1, c-1),(r+1,c+1),(r-1, c+1), (r+1, c-1)]
