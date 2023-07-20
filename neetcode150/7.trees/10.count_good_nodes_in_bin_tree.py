"""4:40pm - 4:44pm"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root, so_far_max):
    if not root:
        return 0

    new_max = max(so_far_max, root.val) 
    indicator = 1 if root.val >= so_far_max else 0
    return indicator + helper(root.left, new_max) + helper(root.right, new_max)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return helper(root, float("-inf"))