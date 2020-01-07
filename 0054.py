from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.append(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        flat_res = [x for sub_list in res for x in sub_list]
        return flat_res


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
