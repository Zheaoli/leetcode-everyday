from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
        if len(pre) == 1 and len(post) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        right_index_pre = pre.index(post[-2])
        root.left = self.constructFromPrePost(
            pre[1:right_index_pre], post[0 : right_index_pre - 1]
        )
        root.right = self.constructFromPrePost(
            pre[right_index_pre:], post[right_index_pre - 1 : -1]
        )
        return root
