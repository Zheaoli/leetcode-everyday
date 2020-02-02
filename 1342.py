from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        counter = {}
        for i in arr:
            counter[i] = counter.setdefault(i, 0) + 1
        counter = {
            k: v
            for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)
        }
        total_count = 0
        result_count = 0
        for i, count in counter.items():
            total_count += count
            result_count += 1
            if total_count >= len(arr) / 2:
                break
        return result_count


print(Solution().minSetSize([1, 9]))
