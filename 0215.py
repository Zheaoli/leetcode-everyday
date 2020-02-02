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
