''' Solution to task from https://www.instagram.com/p/Cal8PwqAnGM/ '''

import unittest

from string import ascii_lowercase, ascii_uppercase

def switch_case(word):
    result = ''
    for char in word:
        if char in ascii_lowercase:
            result += ascii_uppercase[ascii_lowercase.index(char)]
        elif char in ascii_uppercase:
            result += ascii_lowercase[ascii_uppercase.index(char)]
        else:
            result += char
    return result


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(switch_case('Hello world!'), 'hELLO WORLD!')


if __name__ == '__main__':
    unittest.main()
    