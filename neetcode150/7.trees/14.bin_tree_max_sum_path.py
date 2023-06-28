"""11:37am - 11:53am"""

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root: Optional[TreeNode]) -> Tuple[int, Optional[int]]:
    """Returns max_to_root, max_path"""
    if not root:
        return 0, None
    lmax_to_root, lmax = helper(root.left)
    rmax_to_root, rmax = helper(root.right)
    curr_max_to_root = root.val + max(0, lmax_to_root, rmax_to_root)
    max_path = root.val + max(0, lmax_to_root) + max(0, rmax_to_root)
    if lmax is not None:
        max_path = max(max_path, lmax)
    if rmax is not None:
        max_path = max(max_path, rmax)
    return curr_max_to_root, max_path


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return helper(root)[1]