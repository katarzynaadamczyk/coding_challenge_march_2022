''' Solution to task from https://www.instagram.com/p/Caog0rsgkWL/ '''

import unittest

def reverse_string(word):
    return word[::-1]


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_string('Hello world!'), '!dlrow olleH')


if __name__ == '__main__':
    unittest.main()
    