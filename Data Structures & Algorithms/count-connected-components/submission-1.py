class UnionFind:
    def __init__(self):
        self.parentOf = {}
        self.rankOf = {}

    def union(self, n1, n2) -> bool:
        # no union possible/needed
        p1, p2 = self.findPar(n1) , self.findPar(n2)
        if p1 == p2 : return False 
        
        #union needed
        if self.rankOf[p1] == self.rankOf[p2]:
            self.parentOf[p2] = p1
            self.rankOf[p1] +=1
        elif self.rankOf[p1] > self.rankOf[p2]:
            self.parentOf[p2] = p1
        else:
            self.parentOf[p1] = p2
        
        return True

    def findPar(self, node) -> int:
        if node != self.parentOf[node]:
            self.parentOf[node] = self.findPar(self.parentOf[node])
        return self.parentOf[node]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()

        for i in range(n):
            uf.parentOf[i] = i
            uf.rankOf[i] = 0
        
        connectedComponents = n # initially all nodes are treated as connected components of size 1


        for n1, n2 in edges:
            if uf.union(n1, n2):
                # on 
                connectedComponents -= 1
            
        return connectedComponents


        