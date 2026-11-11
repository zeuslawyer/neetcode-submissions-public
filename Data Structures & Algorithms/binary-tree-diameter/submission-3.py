# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxdiameter = 0
        
        # diameter is height of left + height right
        # so we calculate of each subtree recursiviely
        # and compute the diameter along the way.
        def getHeight(node):
            if not node: return 0 # start counting from the leaf

            # get heights.  Note that heights are the max of left and right.  
            # we dont add 1 here because that will inflate diameter.
            left = getHeight(node.left)
            right =  getHeight(node.right)

            # calculate the diameter
            nonlocal maxdiameter
            diameter = left + right
            maxdiameter = max(maxdiameter, diameter)

            # we add 1 here instead.
            heightAtNode = 1 +  max(left, right)
            return heightAtNode
        

        getHeight(root)
        return maxdiameter

