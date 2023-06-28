"""4:34pm - 4:39pm"""
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        
        lrsv, rrsv = self.rightSideView(root.left), self.rightSideView(root.right)
        return [root.val] + rrsv + lrsv[len(rrsv):]
        