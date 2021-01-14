from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, size, window_sum, low, n = sum(nums) - x, -1, 0, -1, len(nums)
        for high, num in enumerate(nums):
            window_sum += num
            while low + 1 < n and window_sum > target:
                low += 1
                window_sum -= nums[low]
            if window_sum == target:
                size = max(size, high - low)
        return -1 if size < 0 else n - size


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, s, cur, res, = (
            len(nums),
            sum(nums),
            0,
            -1,
        )
        target, temp_data = s - x, {0: -1, s: n - 1}
        for i, k in enumerate(nums):
            cur += k
            if (cur - target) in temp_data:
                res = max(res, i - temp_data[cur - target])
            temp_data[cur] = i
        return n - res if res != -1 else -1


print(Solution().minOperations([3, 2, 20, 26, 1, 1, 3], 10))
