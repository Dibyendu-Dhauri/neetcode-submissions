# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def dfs(lower_bound, root, upper_bound):
            if not root:
                return True
            
            if root.val <= lower_bound or root.val >= upper_bound:
                return False

            left = dfs(lower_bound,root.left,root.val)
            right = dfs(root.val,root.right,upper_bound)
            if not left or not right:
                return False
            return True

        
        return dfs(float('-inf'),root,float('inf'))