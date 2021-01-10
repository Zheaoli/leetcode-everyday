from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        results = [first]
        for item in encoded:
            results.append(results[-1] ^ item)
        return results
