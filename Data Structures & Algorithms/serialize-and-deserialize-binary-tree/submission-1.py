# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    # BFS
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res:List[str] = []

        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    # BFS
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        if vals[0] == "N":
            return None
        
        root = TreeNode(int(vals[0]))
        
        q = deque([root])
        index = 1
        # construct tree with BFS
        while q:
            node = q.popleft()
            
            # check left and right are valid vals
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
                
            index +=1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index +=1
        
        return root





