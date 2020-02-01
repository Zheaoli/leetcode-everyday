from typing import Optional
from enum import Enum, unique


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@unique
class Position(Enum):
    left = 0
    right = 1


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None
        self.remove(root, root, None, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root

    def remove(
        self,
        parent: Optional[TreeNode],
        node: Optional[TreeNode],
        position: Optional[Position],
        target: int,
    ) -> None:
        if not node:
            return
        self.remove(node, node.right, Position.right, target)
        self.remove(node, node.left, Position.left, target)
        if parent != node and not node.left and not node.right and node.val == target:
            if position == Position.right:
                parent.right = None
            elif position == Position.left:
                parent.left = None
        return
