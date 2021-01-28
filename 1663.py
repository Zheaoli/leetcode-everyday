import string


class Solution:
    def __init__(self):
        self.char = {}
        self.reverse_char = {}
        for i in range(1, len(string.ascii_lowercase) + 1):
            self.char[string.ascii_lowercase[i - 1]] = i
            self.reverse_char[i] = string.ascii_lowercase[i - 1]

    def getSmallestString(self, n: int, k: int) -> str:
        nums1 = (k - n) // 25
        nums2 = (k - n) % 25
        if (n - nums1 - 1) < 0:
            return "z" * nums1
        return "a" * (n - nums1 - 1) + self.reverse_char[1 + nums2] + "z" * nums1
