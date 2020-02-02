import bisect


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self._data, num)

    def findMedian(self) -> float:
        l = len(self._data)
        median = (self._data[l // 2] + self._data[(l - 1) // 2]) / 2.0
        return median
