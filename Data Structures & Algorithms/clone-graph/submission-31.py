"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# DFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        cloned ={}

        def cloneNode(node):
            # base condition is that the node has already been cloned.
            if node in cloned: return cloned[node]

            newNode = Node(node.val, [])
            cloned[node] = newNode

            for nei in node.neighbors:
                newNode.neighbors.append(cloneNode(nei))
            
            return newNode
        
        cloneNode(node)

        return cloned[node]
        
        