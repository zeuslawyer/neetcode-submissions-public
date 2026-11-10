# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min = -math.inf
        max = math.inf

        return self.validateBST(root, min, max)
    
    def validateBST(self, node, min, max):
        if not node: return True

        if min >= node.val or max <= node.val:
            return False
        
        return (
            self.validateBST(node.left, min, node.val) 
            and self.validateBST(node.right, node.val, max)
        )        


        