class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        temp_array = [0] * (n + 1)
        temp_array[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                temp_array[i] = temp_array[i // 2]
            else:
                temp_array[i] = temp_array[(i - 1) // 2] + temp_array[(i - 1) // 2 + 1]
        return max(temp_array)
