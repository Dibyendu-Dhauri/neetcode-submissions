# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def build_subTree(left,right):
            if left > right:
                return None
            
            nonlocal preorder_index

            val = preorder[preorder_index]
            preorder_index += 1
            inorder_index = inorder_map[val]
            node = TreeNode(val)
            node.left = build_subTree(left,inorder_index-1)
            node.right = build_subTree(inorder_index+1,right)
            return node
        
        return build_subTree(0, len(inorder) - 1)