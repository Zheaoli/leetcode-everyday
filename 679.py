import typing
from operator import add, mul, sub, truediv


class Solution:
    def judgePoint24(self, nums: typing.List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 1e-3
        ops = [add, sub, mul, truediv]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                next_nums = [nums[k] for k in range(len(nums)) if i != k != j]
                for op in ops:
                    if ((op == add or op == mul) and j > i) or (
                        op == truediv and abs(nums[j]) <= 1e-3
                    ):
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums):
                        return True
                    next_nums.pop()
        return False
