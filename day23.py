''' Solution to task from https://www.instagram.com/p/CbcA5qfAurB/ '''

import unittest


def is_ugly(num: int) -> bool:
    return num % 2 == 0 or num % 3 == 0 or num % 5 == 0


class TestAppMethods(unittest.TestCase):
    def testing_is_ugly(self):
        self.assertEqual(is_ugly(2), True)
        self.assertEqual(is_ugly(5), True)
        self.assertEqual(is_ugly(25), True)
        self.assertEqual(is_ugly(9), True)
        self.assertEqual(is_ugly(7), False)
        self.assertEqual(is_ugly(13), False)
        
        
if __name__ == '__main__':
    unittest.main()
    