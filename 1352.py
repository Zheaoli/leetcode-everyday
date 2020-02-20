from typing import List, Dict
import bisect
from operator import mul
from functools import reduce


class ProductOfNumbers:
    _value: List[int]
    _cache_result: Dict[int, int]
    _cache_index: List[int]

    def __init__(self):
        self._value = []
        self._cache_result = {}
        self._cache_index = []

    def add(self, num: int) -> None:
        self._value.append(num)
        self._cache_index.clear()
        self._cache_result.clear()

    def getProduct(self, k: int) -> int:
        if k in self._cache_result:
            return self._cache_result[k]
        cache_index = bisect.bisect(self._cache_index, k)
        if cache_index >= 0:
            last_k = self._cache_index[cache_index]
            result = self._cache_result[last_k]
            for i in range(1, cache_index + 1):
                temp_last_k = last_k + i
                if temp_last_k >= len(self._value):
                    break
                result *= self._value[-last_k]
        else:
            temp_value = (
                self._value[-1 : -k - 1 : -1] if k <= len(self._value) else self._value
            )
            result = reduce(mul, temp_value, 1)
        bisect.bisect_left(self._cache_index, k)
        self._cache_result[k] = result
        return result
