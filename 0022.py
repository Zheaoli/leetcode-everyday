from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.dfs(results, "", n, 0, 0)
        return results

    def dfs(self, results: List[str], temp: str, n: int, left: int, right: int) -> None:
        if right == n:
            results.append(temp)
            return
        if left < n:
            self.dfs(results, temp + "(", n, left + 1, right)
        if right < left:
            self.dfs(results, temp + ")", n, left, right + 1)
