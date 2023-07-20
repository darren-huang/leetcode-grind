"""2:27pm - 3:06pm

took a long while debugging


forgot to update pointer
when doing array assignments if you do
arr[-2] = arr.pop(), note that the index [-2] is calculated AFTER the pop
Mishandled the edge case.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret_str = ""  # action, val |

        def serialize_helper(node):
            nonlocal ret_str
            if not node:
                ret_str += "leaf,None|"
                return

            ret_str += f"new_node_L,{str(node.val)}|"
            serialize_helper(node.left)
            ret_str += "old_node_R,None|"
            serialize_helper(node.right)
            ret_str += "return_to_parent,None|"

        serialize_helper(root)
        print(ret_str[:-1])
        return ret_str[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserialize_helper(parsed_data):
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

        parsed_data = [item.split(",") for item in data.strip().split("|")]
        return deserialize_helper(parsed_data)


# Your Codec object will be instantiated and called as such:
# root = TreeNode(10)
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# print(ans)
