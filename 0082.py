class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-101)
        dummy.next = head
        pre_node = dummy
        cur_node = pre_node.next
        next_node = cur_node.next
        dup = False
        while True:
            if not next_node:
                break
            if cur_node.val != next_node.val:
                if dup:
                    pre_node.next = next_node
                    dup = False
                else:
                    pre_node = cur_node
                cur_node = next_node
                next_node = next_node.next
            else:
                dup = True
                next_node = next_node.next

        if dup is True:
            pre_node.next = next_node
        return dummy.next


node1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(3, next=ListNode(4, next=ListNode(4, next=ListNode(
    5)))))))
Solution().deleteDuplicates(node1)
