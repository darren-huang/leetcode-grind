"""Start 12:00pm

finish 12:13pm

1 bug
did not understand my code that well
path to root vs pass through root

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret_max = None

        def maxPathSumToRoot(given_root):
            nonlocal ret_max
            if given_root is None:
                return 0
            left_max = maxPathSumToRoot(given_root.left)
            right_max = maxPathSumToRoot(given_root.right)
            curr_max = given_root.val + max(left_max, 0) + max(right_max, 0)
            curr_max_to_root = given_root.val + max(left_max, right_max, 0)
            ret_max = max(ret_max, curr_max) if ret_max is not None else curr_max
            return curr_max_to_root

        maxPathSumToRoot(root)

        return ret_max
