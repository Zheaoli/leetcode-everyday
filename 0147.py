class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        temp_list = []
        temp_node = head
        while temp_node:
            temp_list.append(temp_node)
            temp_node = temp_node.next
        for i in range(1, len(temp_list)):
            temp = temp_list[i]
            for j in range(i, -1, -1):
                if temp_list[j - 1].val > temp.val:
                    temp_list[j] = temp_list[j - 1]
                else:
                    temp_list[j] = temp
                    break
                if j == 0:
                    temp_list[j] = temp
        for i in range(len(temp_list)):
            if i == len(temp_list) - 1:
                temp_list[i].next = None
            else:
                temp_list[i].next = temp_list[i + 1]
        return temp_list[0]
