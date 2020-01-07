from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr:
            return False
        length = len(arr)
        visited = [0] * length
        visited[start] = 1
        queue = []
        queue.append(start)
        while queue:
            cur = queue.pop(0)
            if arr[cur] == 0:
                return True
            for i in (-1, 1):
                index = cur + i * arr[cur]
                if index < 0 or index >= length or visited[index] == 1:
                    continue
                queue.append(index)
                visited[index] = 1
        return False
