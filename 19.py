# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        probe = ListNode(0)
        probe.next = head
        slow_head = probe
        fast_head = head
        for _ in range(n - 1):
            if fast_head:
                fast_head = fast_head.next
            else:
                break
        while fast_head.next:
            fast_head = fast_head.next
            slow_head = slow_head.next
        slow_head.next = slow_head.next.next
        return probe.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    s = Solution()
    s.removeNthFromEnd(node1, 2)
