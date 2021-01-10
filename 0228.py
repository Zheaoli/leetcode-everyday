from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        range_item = []
        ranges = []
        for i in nums:
            if not range_item:
                range_item.append(str(i))
                continue
            if i - int(range_item[-1]) > 1:
                ranges.append(range_item)
                range_item = [str(i)]
                continue
            if len(range_item) >= 2:
                range_item.pop()
                range_item.append(str(i))
            else:
                range_item.append(str(i))
        ranges.append(range_item)
        return ["->".join(x) for x in ranges]
