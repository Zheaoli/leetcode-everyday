from typing import Optional, Tuple, List


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNodeWithSum:
    val: int
    left: Optional["TreeNodeWithSum"]
    right: Optional["TreeNodeWithSum"]
    left_sum: int
    right_sum: int

    def __init__(
        self,
        x: int,
        left: Optional["TreeNodeWithSum"],
        right: Optional["TreeNodeWithSum"],
        left_sum: int,
        right_sum: int,
    ):
        self.val = x
        self.left = left
        self.right = right
        self.left_sum = left_sum
        self.right_sum = right_sum


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        total_sum, new_root = self.sum_node(root)
        result = 0
        stack: List[TreeNodeWithSum] = []
        node = new_root
        while node or stack:
            while node:
                stack.append(node)
                result = max(result, ((total_sum - node.left_sum) * node.left_sum))
                result = max(result, ((total_sum - node.right_sum) * node.right_sum))
                node = node.left
            node = stack.pop()
            node = node.right
            if node:
                result = max(result, ((total_sum - node.right_sum) * node.right_sum))
                result = max(result, ((total_sum - node.left_sum) * node.left_sum))
        return result % (10 ** 9 + 7)

    def sum_node(
        self, root: Optional[TreeNode]
    ) -> Tuple[int, Optional[TreeNodeWithSum]]:
        if not root:
            return 0, None
        left_sum, new_left_node = self.sum_node(root.left)
        right_sum, new_right_node = self.sum_node(root.right)
        return (
            left_sum + right_sum + root.val,
            TreeNodeWithSum(
                root.val, new_left_node, new_right_node, left_sum, right_sum
            ),
        )
