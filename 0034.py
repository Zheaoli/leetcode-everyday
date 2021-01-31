from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)
        pivot = right - 1
        sucessor = 0
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                sucessor = i
                break
        nums[pivot], nums[sucessor] = nums[sucessor], nums[pivot]
        self.reverse(nums, pivot + 1, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
