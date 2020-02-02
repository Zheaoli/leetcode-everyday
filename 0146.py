class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.Next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.Next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.Next
            self._remove(n)
            del self.dict[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.Next
        p.Next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.Next = node
        self.tail.prev = node
        node.prev = p
        node.Next = self.tail
