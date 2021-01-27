class Solution:
    def concatenatedBinary(self, n: int) -> int:
        final_result = []
        for i in range(1,n+1):
            final_result.append(bin(i)[2:])
        return int("".join(final_result), 2) % (10 ** 9 + 7)
