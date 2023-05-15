"""12:38
12:54

i have a refusal to code out a sub problem..... 
if there is a sub problem
just code it out plz

and then integrate everything and pray for the best"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same(tree1, tree2):
    if not tree1 or not tree2:
        return tree1 == tree2

    return (
        tree1.val == tree2.val
        and is_same(tree1.left, tree2.left)
        and is_same(tree1.right, tree2.right)
    )


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root == subRoot

        return (
            is_same(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
