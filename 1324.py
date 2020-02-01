from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        str_arr = s.split(" ")
        k = 1
        result = []
        i = 0
        while i < k:
            l = []
            for word in str_arr:
                k = max(k, len(word))
                l.append(word[i] if i < len(word) else " ")
            result.append("".join(l).rstrip())
            i += 1
        return result
