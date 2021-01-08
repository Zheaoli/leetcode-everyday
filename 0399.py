from functools import lru_cache
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        self.data = {}
        self.visited = set()
        for equation, value in zip(equations, values):
            self.data.setdefault(equation[0], {})[equation[1]] = value
            self.data.setdefault(equation[1], {})[equation[0]] = 1 / value
        self.results = []
        for x1, y1 in queries:
            self.results.append(self.search(x1, y1))
        return self.results

    @lru_cache()
    def search(self, start: str, end: str) -> int:
        for item in self.data.setdefault(start, {}).keys():
            if item in self.visited:
                continue
            if item == end:
                return self.data[start][item]
            self.visited.add(item)
            temp_data = self.search(item, end)
            self.visited.remove(item)
            if temp_data != -1:
                return temp_data * self.data[start][item]
        return -1


print(
    Solution().calcEquation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]],
        values=[1.5, 2.5, 5.0],
        queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    )
)
