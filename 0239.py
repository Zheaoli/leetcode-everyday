import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        temp_deque = collections.deque()
        results = []
        for i, n in enumerate(nums):
            while temp_deque and nums[temp_deque[-1]] < n:
                temp_deque.pop()
            temp_deque.append(i)
            if temp_deque[0] == i - k:
                temp_deque.popleft()
            if i >= k - 1:
                results.append(nums[temp_deque[0]])
        return results
