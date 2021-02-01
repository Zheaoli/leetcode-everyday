from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        temp = (sum_b - sum_a) // 2
        set_b = set(B)
        for i in set(A):
            if i + temp in set_b:
                return [i, i + temp]
        return []


print(Solution().fairCandySwap([1, 1], [2, 2]))
