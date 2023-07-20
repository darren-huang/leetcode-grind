"""3:06pm - 3:12pm

added an iterative solution
"""
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret_str = ""  # action, val |

        stack = [root]
        n_processed = defaultdict(int)
        while stack:
            node = stack.pop()
            if node is None:
                ret_str += "leaf,None|"
            elif n_processed[node] == 0:
                # first time processing
                ret_str += f"new_node_L,{str(node.val)}|"
                stack.extend([node, node.left])
                n_processed[node] += 1
            elif n_processed[node] == 1:
                ret_str += "old_node_R,None|"
                stack.extend([node, node.right])
                n_processed[node] += 1
            elif n_processed[node] == 2:
                ret_str += "return_to_parent,None|"

        return ret_str[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        parsed_data = [item.split(",") for item in data.strip().split("|")]

        parents = []
        pointer = 0
        parent_left_bool = []
        while pointer < len(parsed_data) - 1:
            action, val = parsed_data[pointer]
            if action == "new_node_L":
                parents.append(TreeNode(int(val)))
                parent_left_bool.append(True)
            elif action == "old_node_R":
                parent_left_bool[-1] = False
            elif action == "return_to_parent":
                curr = parents.pop()
                parent_left_bool.pop()
                if parent_left_bool[-1]:
                    parents[-1].left = curr
                else:
                    parents[-1].right = curr
            pointer += 1

            # print(action, val, [p.val for p in parents])
        return parents[0] if parents else None


# Your Codec object will be instantiated and called as such:
# root = TreeNode(10)
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# print(ans)
