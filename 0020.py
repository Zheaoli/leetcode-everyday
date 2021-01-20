class Solution:
    def isValid(self, s: str) -> bool:
        temp = {"}": "{", "]": "[", ")": "("}
        results = []
        for i in s:
            if results and i in temp and results[-1] == temp[i]:
                results.pop()
            else:
                results.append(i)
        return len(results) == 0


print(Solution().isValid("()"))
