# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # DFS
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res:List[str] = []

        # DFS, preorder so we always have root -> left -> right.    
        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeList = data.split(",")
        self.idx = 0


        # build tree, pre order traversal
        def dfs():

            val = nodeList[self.idx]

            if val == "N":
                self.idx +=1
                return None
            
            # root
            node = TreeNode(int(val))
            self.idx +=1 

            # left and right
            node.left =dfs()
            node.right = dfs()
            
            return node
        
        return dfs()

            




