"""9:50pm - 9:58pm"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root):
    """returns isbst, min, max"""
    if not root:
        return True, float("inf"), float("-inf")

    lbst, lmin, lmax = helper(root.left)
    rbst, rmin, rmax = helper(root.right)
    is_bst = lbst and rbst and root.val > lmax and root.val < rmin
    return is_bst, min(lmin, root.val), max(rmax, root.val)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root)[0]
