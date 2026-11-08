class UnionFind:
    def __init__(self, n):
        # problem sames there are n-1 edges
        self.parentOf = { i:i for i in range(n+1)}
        self.rankOf ={i : 0 for i in range(n+1)}

    def findParent(self, node) -> int:
        if node != self.parentOf[node]:
            self.parentOf[node] = self.findParent(self.parentOf[node])
        
        return self.parentOf[node]


    def union(self, n1, n2) -> bool:
        p1, p2 = self.findParent(n1), self.findParent(n2)
        
        # no union
        if p1 == p2: return False

        # union based on rank
        r1, r2 = self.rankOf[p1], self.rankOf[p2]
        if r1 == r2:
            self.parentOf[p2] = p1
            self.rankOf[p1] += 1
        elif r1 > r2:
            self.parentOf[p2] = p1
        else:
            self.parentOf[p1] = p2
        
        return True

            


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # problem sames there are n-1 edges
        uf = UnionFind(len(edges))

        for n1, n2 in edges:
            if uf.union(n1, n2): continue
            return [n1, n2]

        