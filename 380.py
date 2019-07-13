import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._map = {}
        self._stack = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._map:
            return False
        length = len(self._stack)
        self._stack.append(val)
        self._map[val] = length
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._map:
            return False
        val_index = self._map[val]
        last_value = self._stack[-1]
        self._stack[val_index], self._stack[self._map[last_value]] = last_value, val
        self._map[last_value] = val_index
        del self._map[val]
        self._stack.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self._stack[random.randint(0, len(self._stack) - 1)]
