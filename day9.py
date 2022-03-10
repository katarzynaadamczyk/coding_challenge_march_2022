''' Solution to task from https://www.instagram.com/p/Ca39KGqgcpV/ '''


import string
import unittest


def mid(word: string) -> string:
    return word[len(word) // 2] if len(word) % 2 else ''


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(mid('doing'), 'i')
        self.assertEqual(mid('doinga'), '')


if __name__ == '__main__':
    unittest.main()
    