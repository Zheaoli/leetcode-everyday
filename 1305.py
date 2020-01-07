from typing import Optional, List


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result_root1 = self.helper(root1)
        result_root2 = self.helper(root2)
        return sorted(result_root1 + result_root2)

    def helper(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result_left = self.helper(root.left)
        result_right = self.helper(root.right)
        result = result_left + result_right
        result.append(root.val)
        return result
