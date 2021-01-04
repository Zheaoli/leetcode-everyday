class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        x, y = 0, 1
        for i in range(n - 1):
            x, y = y, x + y
        return y
