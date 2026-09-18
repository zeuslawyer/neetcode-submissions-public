from collections import deque
import colorsys

class Solution:
    # BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0:
            return image

        original = image[sr][sc]
        if original == color:
            return image

        q = deque()
        q.append((sr, sc))

        while q:
            r, c = q.popleft()

            image[r][c] = color
            
            valids = self.valid_neighbours(r, c, image, original)
            for tup in valids:
                q.append(tup)
        
        return image


    def valid_neighbours(self, r, c, image, original):
        """
        Is within bounds. And also has the origin color that we need to change.
        """
        valids = []
        #up
        if r-1 >= 0 and image[r-1][c] is original:
            valids.append((r-1 ,c))
        
        # down
        if r+1 < len(image) and image[r+1][c] is original :
            valids.append((r+1, c))
        
        # left
        if c-1 >= 0 and image[r][c-1] is  original:
            valids.append((r, c-1))
        
        #right
        if c + 1 <len(image[0]) and image[r][c+1] is  original:
            valids.append((r, c+1))
        
        return valids
        
