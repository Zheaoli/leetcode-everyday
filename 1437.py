from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        last_index = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_index == -1:
                    last_index = i
                    continue
                if i - last_index - 1 < k:
                    return False
                else:
                    last_index = i
        return True
