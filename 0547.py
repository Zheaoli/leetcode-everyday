from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(node):
            if circles[node] == node:
                return node
            root = find(circles[node])
            circles[node] = root
            return root

        n = len(isConnected)
        circles = {x: x for x in range(n)}
        num = n
        for i in range(n):
            for j in range(i, n):
                if i != j and isConnected[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)

        return sum([1 for k, v in circles.items() if k == v])


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
