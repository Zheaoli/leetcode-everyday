class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            temp = self.search(s, i, i)
            if len(temp) > len(result):
                result = temp
            temp = self.search(s, i, i + 1)
            if len(temp) > len(result):
                result = temp
        return result

    @staticmethod
    def search(s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]


Solution().longestPalindrome("babad")
