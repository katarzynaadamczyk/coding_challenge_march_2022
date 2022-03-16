''' Solution to task from https://www.instagram.com/p/CbJ_dlzgPrH/ '''


import string
import unittest


# case-sensitive
def is_palindrome_v1(word: string) -> bool:
    return word == word[::-1]


# case-insensitive
def is_palindrome_v2(word: string) -> bool:
    return word.lower() == word.lower()[::-1]


class TestAppMethods(unittest.TestCase):
    def testing_is_palindrome_v1(self):
        self.assertEqual(is_palindrome_v1('test'), False)
        self.assertEqual(is_palindrome_v1('kayaK'), False)
        self.assertEqual(is_palindrome_v1('kayak'), True)
        
    def testing_is_palindrome_v2(self):
        self.assertEqual(is_palindrome_v2('test'), False)
        self.assertEqual(is_palindrome_v2('kayaK'), True)
        self.assertEqual(is_palindrome_v2('kayak'), True)
        
if __name__ == '__main__':
    unittest.main()
    