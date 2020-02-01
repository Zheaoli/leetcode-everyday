from typing import List, Tuple, Dict
from heapq import heappop, heappush
from collections import defaultdict


class Graph:
    children: defaultdict
    weight: Dict[Tuple[int, int], int]

    def __init__(self, edges) -> None:
        self.children = defaultdict(list)
        self.weight = {}
        for i, j, w in edges:
            self.children[i].append(j)
            self.children[j].append(i)
            self.weight[(i, j)] = w
            self.weight[(j, i)] = w

    def num_neighbor(self, i: int, thres: int, n: int) -> int:
        pq = [(0, i)]
        visited = set()
        while pq:
            dis, node = heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for child in self.children[node]:
                new_dis = self.weight[(node, child)] + dis
                if new_dis > thres:
                    continue
                heappush(pq, (new_dis, child))
        return len(visited) - 1


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = Graph(edges)
        res = [(graph.num_neighbor(i, distanceThreshold, n), -1 * i) for i in range(n)]
        return min(res)[-1] * -1
