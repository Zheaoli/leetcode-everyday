from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        min_sub = num
        result = []
        for i in range(1, int((num + 2) / 2) + 1):
            if (num + 1) % i == 0:
                temp1, temp2 = i, int((num + 1) / i)
                if temp1 == temp2:
                    return [temp1, temp2]
                abs_sub = abs(temp1 - temp2)
                if abs_sub <= min_sub:
                    min_sub = abs_sub
                    result = [temp1, temp2]
            if (num + 2) % i == 0:
                temp1, temp2 = i, int((num + 2) / i)
                if temp1 == temp2:
                    return [temp1, temp2]
                abs_sub = abs(temp1 - temp2)
                if abs_sub <= min_sub:
                    min_sub = abs_sub
                    result = [temp1, temp2]
        return result


print(Solution().closestDivisors(1))
