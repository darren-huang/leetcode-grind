"""3:18pm 4:00pm - ate lunch in between

leetcode serialization

"""


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
        ret_arr = []
        last_layer = [root]
        while last_layer:
            next_layer = []
            for node in last_layer:
                if node:
                    ret_arr.append(node.val)
                    next_layer.append(node.left)
                    next_layer.append(node.right)
                else:
                    ret_arr.append(None)
            last_layer = next_layer

        return str(ret_arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        parsed = [i.strip() for i in data[1:-1].split(",")]
        if parsed[0] == "None":
            return None

        root = TreeNode(int(parsed[0]))
        last_layer = [root]
        pointer = 1
        while pointer < len(parsed):
            next_layer = []
            for p in last_layer:
                if parsed[pointer] != "None":
                    next_layer.append(TreeNode(int(parsed[pointer])))
                    p.left = next_layer[-1]
                if parsed[pointer + 1] != "None":
                    next_layer.append(TreeNode(int(parsed[pointer + 1])))
                    p.right = next_layer[-1]
                pointer += 2
            last_layer = next_layer

        return root


# Your Codec object will be instantiated and called as such:
# root = TreeNode(10)
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# print(ans)
