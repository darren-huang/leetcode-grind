"""12:56
1:17pm
but i solved this much quicker tbh

bug was got the input variable types wrong"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lca_helper(root, p, q):
    if not root:
        return None, False, False

    l_answer, l_has_p, l_has_q = lca_helper(root.left, p, q)
    r_answer, r_has_p, r_has_q = lca_helper(root.right, p, q)

    if l_answer is not None:
        return l_answer, None, None
    elif r_answer is not None:
        return r_answer, None, None

    has_q = root == q or l_has_q or r_has_q
    has_p = root == p or l_has_p or r_has_p
    answer = root.val if has_p and has_q else None

    return answer, has_p, has_q


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        lca, _, _ = lca_helper(root, p, q)
        return lca


if __name__ == "__main__":
    # input = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    # print(Solution().lowestCommonAncestor(input, 2, 3))
    pass
