# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        
        self.insert(root, val)

        return root
    

    def insert(self, node, val):
        if not node:
            return None
        
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val=val)
            else:
                self.insert(node.right, val)
        else:
            if not node.left:
                node.left = TreeNode(val=val)
            else:
                self.insert(node.left, val)
        