import collections
from typing import Tuple

class AnagramChecker:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2

    def _sanitize_input(self, word: str) -> str:
        return word.lower().replace(" ", "")

    def _are_anagrams(self, word1: str, word2: str) -> bool:
        return collections.Counter(word1) == collections.Counter(word2)

    def check_anagrams(self) -> Tuple[bool, str]:
        sanitized_word1 = self._sanitize_input(self.word1)
        sanitized_word2 = self._sanitize_input(self.word2)

        if not sanitized_word1.isalpha() or not sanitized_word2.isalpha():
            return False, "Both words must contain only alphabetic characters."

        if len(sanitized_word1) != len(sanitized_word2):
            return False, "Words must be of the same length to be anagrams."

        return self._are_anagrams(sanitized_word1, sanitized_word2), ""

# Usage
checker = AnagramChecker("listen", "silent")
are_anagrams, message = checker.check_anagrams()
if are_anagrams:
    print("The words are anagrams.")
else:
    print(f"Not anagrams: {message}")
