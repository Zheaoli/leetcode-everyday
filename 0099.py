# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    first: Optional["TreeNode"]
    second: Optional["TreeNode"]

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first: Optional["TreeNode"] = None
        self.second: Optional["TreeNode"] = None
        self.prev = TreeNode(float("-inf"))

        def inorder(node: Optional["TreeNode"]):
            if node:
                if node:
                    inorder(node.left)
                    if self.prev.val >= node.val:
                        self.first = self.first or self.prev
                        self.second = node
                    self.prev = node
                    inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
