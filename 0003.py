class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        if s == "":
            return 0
        index_begin = index_repeat = 0
        count = 1
        max = 1
        cur = ""
        for i in range(1, len(s)):
            cur = s[i]
            curmax_string = s[index_begin : index_begin + count]
            if cur not in curmax_string:
                count += 1
                if count > max:
                    max = count
            else:
                index_repeat = curmax_string.find(cur)
                count -= index_repeat
                index_begin = index_begin + index_repeat + 1
        return max
