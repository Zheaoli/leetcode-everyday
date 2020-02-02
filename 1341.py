from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not mat:
            return []
        number = []
        for i in range(len(mat)):
            number.append((int("".join([str(x) for x in mat[i]]), 2), i))
        number.sort()
        return [x for _, x in number[0:k]]


Solution().kWeakestRows(
    [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    3,
)
