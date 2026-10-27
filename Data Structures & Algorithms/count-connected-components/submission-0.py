class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = {i:i for i in range(n)}
        self.ranks = {i:0 for i in range(n)}
        totalComponents = n # assume they're all distinct

        for n1, n2 in edges:
            if self.union(n1, n2):
                # one less disconnected component
                totalComponents -= 1
        
        return totalComponents
                

    
    def findParent(self,  node:int) -> int:
            if self.parents[node] == node: return self.parents[node]
            
            # assignment is essential for path compression
            self.parents[node] = self.findParent(self.parents[node])
            return self.parents[node]
        
    def union(self,n1, n2) -> bool:
        #store parent values as they're needed
        # union algo ONLY deals with roots
        root1 = self.findParent(n1) 
        root2 =  self.findParent(n2)
        if root1 == root2 : return False

        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = self.parents[root1]
        elif self.ranks[root2] > self.ranks[root1]:
            self.parents[root1] = self.parents[root2]
        
        if self.ranks[root1] == self.ranks[root2]:
            self.parents[root2] = self.parents[root1]
            self.ranks[root1] += 1
        
        return True