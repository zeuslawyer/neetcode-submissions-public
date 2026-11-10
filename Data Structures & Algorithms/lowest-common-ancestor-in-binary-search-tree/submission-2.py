# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root: return None

        if root.val < p.val and root.val < q.val:
            # look in the right sub tree for LCA of p and q
            return self.lowestCommonAncestor(root.right, p, q)
        
        if root.val > p.val and root.val > q.val:
            # look in the left subtree for the LCA
            return self.lowestCommonAncestor(root.left, p, q)
        
        # they are in an ordered way now so this is the root
        return root

        