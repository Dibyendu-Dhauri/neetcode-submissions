# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSame(root,subRoot):
            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                return checkSame(root.left,subRoot.left) and checkSame(root.right, subRoot.right)
            else:
                return False
        
        def dfs(root):
            if not root:
                return False
            
            if checkSame(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)

        return dfs(root)