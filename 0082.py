class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode(-101)
        data = set()
        while head:
            if head.val not in data:
                if head.next and head.next.val == head.val:
                    data.add(head.val)
                    continue
                cur.next = head
                cur = cur.next
                data.add(head.val)
                head = head.next
                cur.next = None
                continue
            head = head.next
        return dummy.next


node1 = ListNode(1, next=ListNode(2, next=ListNode(2)))
Solution().deleteDuplicates(node1)
