# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root):
            nonlocal ans
            if not root:
                ans.append('N')
                return
            
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if(val[i] == 'N'):
                i += 1
                return None

            root = TreeNode(int(val[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        
        return TreeNode(2)
