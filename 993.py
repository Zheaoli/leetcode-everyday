# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.m = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return dx == dy and px != py

    def dfs(self, root, parent, depth):
        if not root:
            return
        self.m[root.val] = (parent, depth)
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)
