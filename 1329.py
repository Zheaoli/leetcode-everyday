import collections
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        data = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                data[i - j].append(mat[i][j])
        for value in data.values():
            value.sort()
        for i in range(n):
            for j in range(m):
                mat[i][j] = data[i - j].pop(0)
        return mat
