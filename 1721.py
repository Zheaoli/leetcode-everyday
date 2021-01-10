from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        nodes: List[ListNode] = []
        dummy = head
        while head:
            nodes.append(head)
            head = head.next
        nodes[k - 1].val, nodes[len(nodes) - k].val = (
            nodes[len(nodes) - k].val,
            nodes[k - 1].val,
        )
        return dummy
