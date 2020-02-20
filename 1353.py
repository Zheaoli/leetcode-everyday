from typing import List, Set


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        events.sort(key=lambda x: x[1])
        day_set: Set[int] = set()
        result = 0
        for i in events:
            for j in range(i[0], i[1]):
                if j not in day_set:
                    result += 1
                    day_set.add(j)
                    break
        return result


print(Solution().maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
