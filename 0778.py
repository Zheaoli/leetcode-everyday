import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heap = [(grid[0][0], 0, 0)]
        res = 0
        seen = {(0, 0)}
        length = len(grid)
        while True:
            temp_time, i, j = heapq.heappop(heap)
            res = max(res, temp_time)
            if i == length - 1 and j == length - 1:
                return res
            for x, y in directions:
                if (
                    0 <= x + i <= length - 1
                    and 0 <= y + j <= length - 1
                    and (x + i, y + j) not in seen
                ):
                    heapq.heappush(heap, (grid[x + i][y + j], x + i, y + j))
                    seen.add((x + i, y + j))
