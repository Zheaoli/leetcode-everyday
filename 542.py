from typing import *


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        distance = []
        for i in range(len(matrix)):
            temp_distances = []
            for j in range(len(matrix[0])):
                temp_distances.append(65535)
            distance.append(temp_distances)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                    continue
                self.get_distance(matrix, i, j, distance)
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                    continue
                self.get_distance(matrix, i, j, distance, 1)
        return distance

    def get_distance(self,
                     matrix: List[List[int]],
                     x: int,
                     y: int,
                     distance: List[List[int]],
                     left_or_right=0):
        position = []
        direction = [(-1, 0), (0, -1)] if left_or_right == 0 else [(-1, 0),
                                                                   (0, -1),
                                                                   (1, 0),
                                                                   (0, 1)]
        for d_x, d_y in direction:
            f_x, f_y = x + d_x, y + d_y
            if f_x < 0 or f_x >= len(matrix) or f_y < 0 or f_y >= len(
                    matrix[0]):
                continue
            position.append((f_x, f_y))
        if position:
            distance[x][y] = min([distance[t_x][t_y]
                                  for t_x, t_y in position]) + 1
