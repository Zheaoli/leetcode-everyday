class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []

    def push(self, x: int) -> None:
        if not self._data:
            self._data.append([x, x])
        else:
            self._data.append([x, min(self._data[-1][1], x)])

    def pop(self) -> None:
        self._data.pop()

    def top(self) -> int:
        if self._data:
            return self._data[-1][0]

    def getMin(self) -> int:
        return self._min[-1][1]
