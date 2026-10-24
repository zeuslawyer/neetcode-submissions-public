class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank ={}
        self.numComponents = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

        

    def find(self, x: int) -> int:
        # all nodes parent's should point to root -- this is path compression.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y): return False

        px, py = self.find(x), self.find(y)
        rx, ry = self.rank[px], self.rank[py]

        if rx > ry:
            # IMPORTANT:  update the parent not the node itself
            self.parent[py] = px
        elif ry > rx:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1

        self.numComponents -= 1

        return True
        

    def getNumComponents(self) -> int:
        # return len(self.rank.values())
        return self.numComponents
