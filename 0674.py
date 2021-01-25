from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        if not nums:
            return 0
        temp_count = 0
        last_num = float("-inf")
        for i in nums:
            if i > last_num:
                temp_count += 1
            else:
                result = max(result, temp_count)
                temp_count = 1
            last_num = i
        result = max(temp_count, result)
        return result


print(Solution().findLengthOfLCIS([1, 3, 5, 7]))
