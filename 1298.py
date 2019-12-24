import collections
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        owned_keys = set()
        queue = collections.deque(initialBoxes)
        res = 0
        record = dict()
        while queue:
            cur = queue.popleft()
            if status[cur] or cur in owned_keys:
                for key in keys[cur]:
                    owned_keys.add(key)
                for box in containedBoxes[cur]:
                    queue.append(box)
                res += candies[cur]
            else:
                if cur in record and record[cur] == owned_keys:
                    break
                queue.append(cur)
                record[cur] = owned_keys
        return res
