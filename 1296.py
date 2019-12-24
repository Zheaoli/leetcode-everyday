from typing import List
import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        for key in sorted(c):
            while c[key]:
                for key1 in range(key, key + k):
                    if not c[key1]:
                        return False
                    c[key1] -= 1
        return True
