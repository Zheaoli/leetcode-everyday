import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)
        head = dummy = ListNode()
        while heap:
            _, i, temp_node = heapq.heappop(heap)
            if temp_node.next:
                heapq.heappush(heap, (temp_node.next.val, i, temp_node.next))
            dummy.next = temp_node
            dummy = dummy.next
        return head.next
