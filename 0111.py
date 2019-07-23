class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.min = 99999
        self.cur = 0
        self.deep(root)
        return self.min

    def deep(self, node: TreeNode) -> None:
        if not node:
            self.min = self.cur
            return
        self.cur += 1
        if not node.left and not node.right and self.cur < self.min:
            self.min = self.cur
        if node.left:
            self.deep(node.left)
        if node.right:
            self.deep(node.right)
        self.cur -= 1
