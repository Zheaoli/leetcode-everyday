class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not ListNode:
            return 0
        temp_head = head
        values = []
        while temp_head:
            values.append(temp_head.val)
            temp_head = temp_head.next
        results = 0
        values = values[::-1]
        for i in range(len(values) - 1, -1, -1):
            results += 2 ** i * values[i]
        return results
