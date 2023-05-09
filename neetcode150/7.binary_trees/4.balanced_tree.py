"""12:29pm- 12:33pm"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced_helper(root):
    if not root:
        return True, -1

    l_is_balanced, l_height = is_balanced_helper(root.left)
    r_is_balanced, r_height = is_balanced_helper(root.right)
    is_balanced = abs(l_height - r_height) <= 1 and l_is_balanced and r_is_balanced
    height = 1 + max(l_height, r_height)

    return is_balanced, height


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = is_balanced_helper(root)
        return is_balanced
