from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        length = len(jobs)
        jobs.sort(reverse=True)
        left, right = max(jobs), sum(jobs)
        while left < right:
            x = (left + right) // 2
            cap = [x] * k
            if self.search(0, cap, x, length, k, jobs):
                right = x
            else:
                left = x + 1
        return left

    def search(
        self,
        i: int,
        cap: List[int],
        x: int,
        length: int,
        worker_count: int,
        jobs: List[int],
    ) -> bool:
        if i == length:
            return True
        for j in range(worker_count):
            if cap[j] >= jobs[i]:
                cap[j] -= jobs[i]
                if self.search(i + 1, cap, x, length, worker_count, jobs):
                    return True
                cap[j] += jobs[i]
            if cap[j] == x:
                return False
        return False


print(Solution().minimumTimeRequired([1, 2, 4, 7, 8], 2))
