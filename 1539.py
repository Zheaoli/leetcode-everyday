from typing import List

MAX_INT = 9223372036854775807


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        data = set(arr)
        count = 0
        for i in range(1, MAX_INT):
            if i not in data:
                count += 1
                if count == k:
                    return i
        return count
