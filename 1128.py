from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        result = 0
        for i in dominoes:
            temp = tuple(sorted(i))
            result += d.setdefault(temp, 0)
            d[temp] += 1
        return result
