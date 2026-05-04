"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clone_map = {}
        def dfs(node,clone_map):
            if node in clone_map:
                return clone_map[node]

            clone_node = Node(node.val)
            clone_map[node] = clone_node

            for neighbors in node.neighbors:
                clone_neighbors = dfs(neighbors,clone_map)
                clone_node.neighbors.append(clone_neighbors)
            return clone_node
        return dfs(node,clone_map) if node else None
        
