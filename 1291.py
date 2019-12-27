from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        min_size = len(str(low))
        max_size = len(str(high))
        flag = "123456789"
        for i in range(min_size, max_size + 1):
            for j in range(10 - i):
                temp_value = int(flag[j : j + i])
                if i == min_size and temp_value < low:
                    continue
                if i == max_size and temp_value > high:
                    break
                results.append(temp_value)
        return results


print(Solution().sequentialDigits(100, 300))
