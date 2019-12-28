from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        results = []
        results.append(-1)
        arr = arr[::-1]
        for i in range(1, len(arr)):
            results.append(max(arr[i - 1], results[-1]))
        return results[::-1]
