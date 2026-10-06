# Definition for a binary tree node.
# class TreeNode:
#     def __init__(ItemsView, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def validate(leftval, node, rightval):
            if not node: return True

            # assert BST property
            if not leftval < node.val < rightval:
                return False
            
            # travel subtrees
            return validate(leftval, node.left, node.val) and validate(node.val, node.right, rightval)


        return validate(-math.inf, root, math.inf)

       
        

