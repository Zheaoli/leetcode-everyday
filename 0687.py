from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.get_path(root)
        return self.res

    def get_path(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.get_path(root.left)
        right = self.get_path(root.right)
        pl, pr = 0, 0
        if root.left and root.left.val == root.val:
            pl = 1 + left
        if root.right and root.right.val == root.val:
            pr = 1 + right
        self.res = max(self.res, pl + pr)
        return max(pl, pr)
