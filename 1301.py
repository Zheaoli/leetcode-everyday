from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        outList = []
        while queue:
            res = []
            nextQueue = []
            for point in queue:
                res.append(point.val)
                if point.left:
                    nextQueue.append(point.left)
                if point.right:
                    nextQueue.append(point.right)
            outList.append(res)
            queue = nextQueue
        return sum(outList[-1])
