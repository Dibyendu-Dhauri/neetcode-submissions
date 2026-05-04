"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mp = {}
        def dfs(node):
            if node in mp:
                return mp[node]

            clone_node = Node(node.val)
            mp[node] = clone_node

            for neighbors in node.neighbors:
                clone_neighbors = dfs(neighbors)
                clone_node.neighbors.append(clone_neighbors)
            return clone_node
        return dfs(node) if node else None
        
