import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_word1 = collections.Counter(word1)
        counter_word2 = collections.Counter(word2)
        return set(counter_word1.keys()) == set(
            counter_word2.keys()
        ) and collections.Counter(counter_word1.values()) == collections.Counter(
            counter_word2.values()
        )


print(Solution().closeStrings("cabbba", "abbccc"))
