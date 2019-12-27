from typing import List


class Solution:
    def maxSideLength(self, A: List[List[int]], t: int) -> int:
        r, c = len(A), len(A[0])
        pre = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                pre[i][j] = (
                    pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + A[i - 1][j - 1]
                )

        res = l = 0
        temp_func = (
            lambda x1, y1, x2, y2: pre[x2][y2]
            - pre[x2][y1 - 1]
            - pre[x1 - 1][y2]
            + pre[x1 - 1][y1 - 1]
        )
        for x in range(1, r + 1):
            for y in range(1, c + 1):
                k = res
                while y + k <= c and x + k <= r:
                    if temp_func(x, y, x + k, y + k) > t:
                        break
                    res = max(res, k + 1)
                    k += 1
        return res
