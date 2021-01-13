from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        start, end = 0, len(people) - 1
        while start <= end:
            if people[start] + people[end] <= limit:
                end -= 1
            start += 1
        return start


print(Solution().numRescueBoats([3, 2, 2, 1], 3))
