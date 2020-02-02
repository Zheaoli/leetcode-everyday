from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        length = len(arr)
        dp = [1] * length
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < length and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
