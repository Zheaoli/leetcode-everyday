# Definition for a binary tree node.
from typing import Tuple, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        return self.search_node(cloned, self.search_point(original, target))

    def search_point(self, original: TreeNode, target: TreeNode) -> Tuple[int, int]:
        queue = [original]
        level = 0
        while queue:
            count = 0
            level += 1
            next_queue = []
            for item in queue:
                count += 1
                if item == target:
                    return (level, count)
                if item.left:
                    next_queue.append(item.left)
                if item.right:
                    next_queue.append(item.right)
            queue = next_queue
        return -1, -1

    def search_node(
        self, cloned: TreeNode, position: Tuple[int, int]
    ) -> Optional[TreeNode]:
        queue = [cloned]
        level = 0
        while queue:
            count = 0
            level += 1
            next_queue = []
            for item in queue:
                count += 1
                if level == position[0] and count == position[1]:
                    return item
                if item.left:
                    next_queue.append(item.left)
                if item.right:
                    next_queue.append(item.right)
            queue = next_queue
