''' Solution to task from https://www.instagram.com/p/CajX3LZAO5m/  '''

import unittest

def lowercase(word):
    return word.lower()


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(lowercase('Hello world!'), 'hello world!')


if __name__ == '__main__':
    unittest.main()
    