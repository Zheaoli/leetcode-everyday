class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return False if self.check_dep(root)==-1 else True
    def check_dep(self,root:TreeNode)->int:
        if not root:
            return 0
        left = self.check_dep(root.left)
        if left==-1:
            return -1
        right=self.check_dep(root.right)
        if right==-1:
            return -1
        diff=abs(left-right)
        if diff>1:
            return -1
        else:
            return 1+max(left,right)
        