"""
3:28pm
3:38pm
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        new_graph = Node(node.val)

        # run dfs on node
        new_node_dict = {node.val: new_graph}
        stack = [(node, new_graph)]

        while stack:
            orig, copy = stack.pop()
            for neighbor in orig.neighbors:
                if neighbor.val not in new_node_dict:
                    new_node_dict[neighbor.val] = Node(neighbor.val)
                    stack.append((neighbor, new_node_dict[neighbor.val]))
                copy.neighbors.append(new_node_dict[neighbor.val])

        return new_graph
