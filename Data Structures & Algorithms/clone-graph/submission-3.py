"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#DFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloneOf = {}

        # DFS    
        def recursivelyClone(node):
            if not node: return None

            if node in cloneOf:
                return cloneOf[node]
            
            clone = Node(node.val)
            cloneOf[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(recursivelyClone(n))
            
            return clone
            
        
        return recursivelyClone(node)

