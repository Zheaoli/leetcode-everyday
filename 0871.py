import heapq


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        stations.append([target, float("inf")])
        que = []
        tank = startFuel
        res = 0
        prev = 0
        for p, g in stations:
            tank -= p - prev
            while que and tank < 0:
                tank += -heapq.heappop(que)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(que, -g)
            prev = p
        return res
