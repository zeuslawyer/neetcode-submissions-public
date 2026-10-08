# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # reference jenny's lecture: https://www.youtube.com/watch?v=PoBGyrIWisE
        # KEY PROPERTIES:
        # preorder array is  [node][...left tree][ ...righttree]
        # inorder array is [...left tree][node][ ...righttree]
        # so INORDER array has the root node nestled between subarrays a
        # but PREORDER has a sequence that gives us the root node for each sub tree
        # we can just WALK throough PREORDER then use INORDER to calculate the left and right subtrees for each PREORDER root note
        

        if not inorder or not preorder: return None
        
        # optimization to avoide .index() hunting
        # store indexes from inorder array as that gives us index of the root value each time
        inorderIndexOf = {val: i for i, val in enumerate(inorder)}

        self.pre_index = 0 # pointer that iterates over PREORDER. PREORDER always starts with root
        
        # optimisation:  left and right are pointers that delineate inorder left tree and right tree starts and ends.
        def dfs(left, right):
            if left > right: return # base condition. Only real use for left and right.
            
            rootvalue= preorder[self.pre_index]
            root = TreeNode(rootvalue)

            root_index = inorderIndexOf[rootvalue]

            self.pre_index+=1
            
            root.left = dfs(left, root_index-1)
            root.right = dfs(root_index+1, right)

            return root

        return dfs(0, len(inorder)-1)

            
        
       



