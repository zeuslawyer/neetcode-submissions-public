# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val=val)
                    break
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val=val)
                    break
                curr = curr.left

        return root       



    # # Recursion
    # def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root:
    #         return TreeNode(val=val)
        
    #     self.insert(root, val)

    #     return root
    

    # def insert(self, node, val):
    #     if not node:
    #         return None
        
    #     if val > node.val:
    #         if not node.right:
    #             node.right = TreeNode(val=val)
    #         else:
    #             self.insert(node.right, val)
    #     else:
    #         if not node.left:
    #             node.left = TreeNode(val=val)
    #         else:
    #             self.insert(node.left, val)
        