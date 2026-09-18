from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0:
            return [[]]

        original = image[sr][sc]
        if color == original:
            return image

        
        # bfs
        q = deque()
        q.append((sr, sc))
        
        while q:
            r, c = q.popleft()
            image[r][c] = color

            neighbours = self.valid_neighbours(r,c, image, original)
            for n in neighbours:
                if not n:
                    continue

                q.append(n)


        return image


    def valid_neighbours(self, r, c, image, original):
        valids = []
        
        # left
        if c -1 >= 0 and  image[r][c-1] == original:
                valids.append((r, c-1))
        
        # right
        if c+1 < len(image[0]) and image[r][c+1] == original:
            valids.append((r, c+1))

        # up
        if r -1 >= 0 and image[r-1][c] == original:
            valids.append((r-1, c ))
    

        # down
        if r+1 < len(image) and image[r+1][c] == original:
            valids.append((r+1, c))
        
        return valids


        




        
