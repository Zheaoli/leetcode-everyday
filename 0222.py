# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.count(root)

    def count(self, node: TreeNode):
        if not node:
            return 0
        left_count = self.count(node.left)
        right_count = self.count(node.right)
        return 1 + left_count + right_count
