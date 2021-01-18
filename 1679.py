from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        for item, value in counter.items():
            if value > 0:
                if (k - item) in counter:
                    if k - item != item:
                        temp_count = min(value, counter[k - item])
                        count += temp_count
                        counter[k - item] -= temp_count
                        counter[item] -= temp_count
                    else:
                        temp_count = value // 2
                        counter[item] -= temp_count
                        count += temp_count
        return count
