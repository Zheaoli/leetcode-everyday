class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def pre_order(root):
            if not root:
                val.append("*")
            else:
                vals.append(str(root.val))
                pre_order(root.left)
                pre_order(root.right)

        pre_order(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        import collections

        vals = collections.deque(val for val in data.split(","))

        def build():
            if vals:
                val = vals.popleft()
                if val == "*":
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root

        return build()
