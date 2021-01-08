class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp_index1 = 0
        temp_index2 = 0
        main_index1 = 0
        main_index2 = 0
        while main_index1 < len(word1) and main_index2 < len(word2):
            while temp_index1 < len(word1[main_index1]) and temp_index2 < len(
                word2[main_index2]
            ):
                if word1[main_index1][temp_index1] != word2[main_index2][temp_index2]:
                    return False
                temp_index1 += 1
                temp_index2 += 1
            if temp_index1 >= len(word1[main_index1]) and main_index1 < len(word1):
                main_index1 += 1
                temp_index1 = 0
            if temp_index2 >= len(word2[main_index2]) and main_index2 < len(word2):
                main_index2 += 1
                temp_index2 = 0
        if main_index1 < len(word1) or main_index2 < len(word2):
            return False
        return True
