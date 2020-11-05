import collections
from typing import List, Dict, Set
from collections import deque
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words: Set[str] = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))
        visited: Set[str] = set()
        chars: str = ascii_lowercase
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in chars:
                    new_word = f"{word[:i]}{char}{word[i+1:]}"
                    if new_word in words and new_word not in visited:
                        queue.append((new_word, length + 1))
                        visited.add(new_word)
        return 0
