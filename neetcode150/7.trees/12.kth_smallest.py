# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def helper(node, k):
    # base case
    if not node:
        return 0, None

    # check left side
    l_count, l_ksmallest = helper(node.left, k)
    if l_ksmallest is not None:
        return None, l_ksmallest
    elif k == l_count + 1:
        return None, node.val

    # check right side
    r_count, r_ksmallest = helper(node.right, k - l_count - 1)
    if r_ksmallest is not None:
        return None, r_ksmallest

    # neither contains the correct kth smallest
    return l_count + r_count + 1, None


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, k_smallest = helper(root, k)
        return k_smallest
