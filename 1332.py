class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        length = self.manacher(s)
        if length == 1:
            return len(s)

        return len(s) - length + 1

    def manacher(self, s: str) -> int:
        s = "#" + "#".join(s) + "#"
        right_length = [0] * len(s)
        max_right = 0
        pos = 0
        max_len = 0
        for i in range(len(s)):
            if i < max_right:
                right_length[i] = min(right_length[2 * pos - i], max_right - i)
            else:
                right_length[i] = 1
            while (
                i - right_length[i] >= 0
                and i + right_length[i] < len(s)
                and s[i - right_length[i]] == s[i + right_length[i]]
            ):
                right_length[i] += 1
            if right_length[i] + i - 1 > max_right:
                max_right = right_length[i] + i - 1
                pos = i
            max_len = max(max_len, right_length[i])
        return max_len - 1
