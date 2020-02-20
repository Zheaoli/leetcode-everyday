import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if not target:
            return False
        total = sum(target)
        target = sorted([-x for x in target])
        heapq.heapify(target)
        while True:
            a = -heapq.heappop(target)
            total -= a
            if a == 1 or total == 1:
                return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(target, -a)
