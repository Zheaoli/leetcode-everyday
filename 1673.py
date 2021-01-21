from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for index, value in enumerate(nums):
            while (
                stack and stack[-1] > value and len(stack) - 1 + len(nums) - index >= k
            ):
                stack.pop()
            if len(stack) < k:
                stack.append(value)
        return stack
