from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional["TreeNode"]) -> int:
        self.res = 0
        self.dfs(root, -1, 999999999)
        return self.res

    def dfs(self, node: Optional["TreeNode"], max_value: int, min_value: int):
        if not node:
            self.res = max(self.res, max_value - min_value)
            return
        self.dfs(node.left, max(node.val, max_value), min(node.val, min_value))
        self.dfs(node.right, max(node.val, max_value), min(node.val, min_value))
