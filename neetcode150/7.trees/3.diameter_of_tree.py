"""12:17pm
12:26pm - bit slow on the debugging

check values for base case are correct"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_helper(root):
    if not root:
        return -1, -1

    max_seen1, max_to_root1 = diameter_helper(root.left)
    max_seen2, max_to_root2 = diameter_helper(root.right)
    max_to_root = 1 + max(max_to_root1, max_to_root2)
    max_seen = max(max_seen1, max_seen2, max_to_root1 + max_to_root2 + 2)
    return max_seen, max_to_root


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_seen, _ = diameter_helper(root)
        return max_seen
