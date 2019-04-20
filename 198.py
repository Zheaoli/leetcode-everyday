class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        money=0
        money1=0
        for i in range(0,len(nums)):
            temp=money
            money=max(money,money1)
            money1=temp+nums[i]
        return max(money,money1)