# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional["TreeNode"]) -> int:
        return max(self.dfs(root))

    def dfs(self, root: Optional["TreeNode"]) -> Tuple[int, int]:
        if not root:
            return (0, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (
            root.val + left[1] + right[1],
            max(left[0], left[1]) + max(right[0], right[1]),
        )
