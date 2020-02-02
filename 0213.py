class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) > 2:
            return max(
                [
                    self.self_rob(nums, 0, len(nums) - 1),
                    self.self_rob(nums, 1, len(nums)),
                ]
            )
        else:
            return max(nums)

    def self_rob(self, nums, start, end):
        money = 0
        money1 = 0
        for i in range(start, end):
            temp = money
            money = max(money, money1)
            money1 = temp + nums[i]
        return max(money, money1)
