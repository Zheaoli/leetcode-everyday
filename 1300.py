from typing import List
from collections import namedtuple
from functools import cmp_to_key


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0
        temp_data = namedtuple("TempData", ["data", "difference"])
        result = []
        origin_length = len(arr)
        min_value = int(round(target / origin_length))
        arr = sorted(arr)
        sum = [0] * origin_length
        sum[0] = arr[0]
        for i in range(1, origin_length):
            sum[i] = sum[i - 1] + arr[i]
        if sum[-1] <= target:
            return arr[-1]
        if min_value <= arr[0]:
            result.append(temp_data(min_value, abs(min_value * origin_length - target)))
        result.append(temp_data(arr[0], abs(arr[0] * origin_length - target)))
        for i in range(1, origin_length):
            if i == origin_length - 1:
                result.append(temp_data(arr[i], abs(sum[i] - target)))
                continue
            temp_min_value = round((target - sum[i] + arr[i]) / (origin_length - i))
            if temp_min_value > arr[i - 1]:
                temp_difference = abs(
                    temp_min_value * (origin_length - i) + sum[i] - arr[i] - target
                )

                result.append(temp_data(temp_min_value, temp_difference))
            result.append(
                temp_data(
                    arr[i], abs(sum[i] - arr[i] + arr[i] * (origin_length - i) - target)
                )
            )
        result = sorted(
            result, key=cmp_to_key(lambda a, b: a.difference - b.difference)
        )
        return result[0].data


print(Solution().findBestValue([1547, 83230, 57084, 93444, 70879], 71237))
