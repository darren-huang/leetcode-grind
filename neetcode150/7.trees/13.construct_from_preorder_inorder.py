# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solution(preorder, inorder):
    node_to_index = {node: i for i, node in enumerate(inorder)}
    root = TreeNode(val=preorder[0])
    curr = root
    stack = []
    i = 1
    while i < len(preorder):
        node = TreeNode(val=preorder[i])
        next_ix = node_to_index[node.val]
        curr_ix = node_to_index[curr.val]
        if next_ix < curr_ix:
            curr.left = node
            stack.append(curr)
            curr = node
        else:  # node is to the RIGHT of curr
            while stack and node_to_index[stack[-1].val] < next_ix:
                curr = stack.pop()
            curr.right = node
            curr = node
        i += 1
    return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return solution(preorder, inorder)
