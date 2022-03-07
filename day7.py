''' Solution to task from https://www.instagram.com/p/Cay1kcugldU/ '''


from string import ascii_uppercase
import unittest


def capital_indexes(word):
    return [index for index, char in enumerate(word) if char in ascii_uppercase]


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(capital_indexes('doing'), [])
        self.assertEqual(capital_indexes('DOING'), [0, 1, 2, 3, 4])
        self.assertEqual(capital_indexes('DOiNG'), [0, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()
    