"""10:22am - 10:27am"""

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ret = []
        while queue:
            ret.append([node.val for node in queue])
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt.left:
                    queue.append(nxt.left)
                if nxt.right:
                    queue.append(nxt.right)
        return ret
