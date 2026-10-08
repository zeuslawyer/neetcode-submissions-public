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
        indexOf = {val: i for i, val in enumerate(inorder)}

        self.pre_index = 0 # track the index of the root in PREORDER which always starts with root
        
        # optimisation:  left and right are pointers that delineate preorder left tree and right tree starts and ends.
        def dfs(left, right):
            if left > right: return
            
            rootvalue= preorder[self.pre_index]
            root = TreeNode(rootvalue)

            tree_root_index = indexOf[rootvalue]

            self.pre_index+=1
            
            root.left = dfs(left, tree_root_index-1)
            root.right = dfs(tree_root_index+1, right)

            return root

        return dfs(0, len(inorder)-1)

            
        
       



