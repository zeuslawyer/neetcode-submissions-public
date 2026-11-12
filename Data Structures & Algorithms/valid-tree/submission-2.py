class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n -1: return False

        adj ={i:[] for i in range(n)}

        for n1, n2 in edges:
            adj.get(n1, []).append(n2)
            adj.get(n2, []).append(n1)

        
        visited = set()
        def dfs(node, par) -> bool:
            if node == None : return True
            
            if node in visited: return False # has cycle. not valid tree.

            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n      


            

        