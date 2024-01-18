import unittest
from anagrams import AnagramChecker
class TestAnagramChecker(unittest.TestCase):
    
    def test_valid_anagram(self):
        checker = AnagramChecker("listen", "silent")
        result, _ = checker.check_anagrams()
        self.assertTrue(result)

    def test_invalid_anagram(self):
        checker = AnagramChecker("hello", "world")
        result, _ = checker.check_anagrams()
        self.assertFalse(result)

    def test_non_alpha_characters(self):
        checker = AnagramChecker("123", "321")
        result, message = checker.check_anagrams()
        self.assertFalse(result)
        self.assertEqual(message, "Both words must contain only alphabetic characters.")

    def test_different_lengths(self):
        checker = AnagramChecker("abc", "abcd")
        result, message = checker.check_anagrams()
        self.assertFalse(result)
        self.assertEqual(message, "Words must be of the same length to be anagrams.")

    def test_case_insensitivity(self):
        checker = AnagramChecker("Listen", "Silent")
        result, _ = checker.check_anagrams()
        self.assertTrue(result)

    def test_space_handling(self):
        checker = AnagramChecker("conversation", "voices rant on")
        result, _ = checker.check_anagrams()
        self.assertTrue(result)

# Run the tests
if __name__ == '__main__':
    unittest.main()