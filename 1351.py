from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n_length = len(grid[0])
        result = 0
        for item in grid:
            for i in range(n_length):
                if item[i] < 0:
                    result += n_length - i
                    break
        return result
