# Definition for a binary tree node.
# class TreeNode:
#     def __init__(ItemsView, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        # start with infinity left and right vals and then update as we move down the tree
        def validate(node, leftval, rightval):
            if not node: return True

            # assert BST property
            if not leftval < node.val < rightval:
                return False
            
            # travel subtrees
            return validate(node.left, leftval, node.val) and validate(node.right, node.val, rightval)


        return validate(root, -math.inf, math.inf)

       
        

