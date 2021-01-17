import random
from typing import List


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        nums = sorted(nums)
        return nums[-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        random.shuffle(nums)
        position = self.partition(nums, 0, len(nums) - 1)
        if position > len(nums) - k:
            return self.findKthLargest(nums[:position], k - (len(nums) - position))
        elif position < len(nums) - k:
            return self.findKthLargest(nums[position + 1 :], k)
        else:
            return nums[position]

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        lo = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[right] = nums[right], nums[lo]
        return lo


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
# print(Solution().partition([5, 6], 0, 1))
