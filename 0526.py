from collections import OrderedDict
from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        results = [0]
        self.search(n, series=OrderedDict(), results=results)
        return results[0]

    def search(self, n: int, series: OrderedDict[int, int], results: List[int]):
        if len(series) == n:
            results[0] += 1
            return
        for i in range(n):
            if i + 1 not in series:
                if ((i + 1) % (len(series) + 1) == 0) or (
                    (len(series) + 1) % (i + 1) == 0
                ):
                    series[i + 1] = i + 1
                    self.search(n, series, results)
                    del series[i + 1]


print(Solution().countArrangement(2))
