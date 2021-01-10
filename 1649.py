from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        max_value = max(instructions)
        tree = [0] * (max_value + 1)
        result = 0
        for i, a in enumerate(instructions):
            result += min(self.query(tree, a - 1), i - self.query(tree, a))
            self.update(tree, a, max_value)
        return result % (10 ** 9 + 7)

    @staticmethod
    def update(tree: List[int], x: int, max_value: int):
        while x <= max_value:
            tree[x] += 1
            x += x & -x

    @staticmethod
    def query(tree: List[int], x: int) -> int:
        result = 0
        while x > 0:
            result += tree[x]
            x -= x & -x
        return result
