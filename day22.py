''' Solution to task from https://www.instagram.com/p/CbZaWNaAa1J/ '''

from tokenize import String
import unittest


def perfectly_balanced(strng: String) -> bool:
    chars = set(list(strng))
    if len(chars) == 2:
        x, y = chars
        return strng.count(x) == strng.count(y) == len(strng) // 2
    return False


class TestAppMethods(unittest.TestCase):
    def testing_perfectly_balanced(self):
        self.assertEqual(perfectly_balanced(''), False)
        self.assertEqual(perfectly_balanced('xxxyyy'), True)
        self.assertEqual(perfectly_balanced('xyyy'), False)
        self.assertEqual(perfectly_balanced('xxy'), False)
        self.assertEqual(perfectly_balanced('xxyz'), False)
        
        
if __name__ == '__main__':
    unittest.main()
    