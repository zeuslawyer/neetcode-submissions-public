# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0

        # in order traversal
        ascending = []

        def inorder(node):
           if not node: return

           inorder(node.left)
           ascending.append(node.val)
           inorder(node.right)

        inorder(root)

        print(ascending)

        # 1-indexed
        return ascending[k-1]


        

        



        
            

        



