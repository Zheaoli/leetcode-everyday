import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        record = collections.defaultdict(int)
        res = 0
        for i in range(len(s) - minSize + 1):
            sub_string = s[i : i + minSize]
            if len(set(sub_string)) <= maxLetters:
                record[sub_string] += 1
                res = max(res, record[sub_string])
        return res
