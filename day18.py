''' Solution to task from https://www.instagram.com/p/CbPJvcFgAqV/ '''

from typing import List
import unittest

# one-liner
def all_equal_v1(lstofnums: List[int]) -> bool:
    return len(set(lstofnums)) == 1

# loop version
def all_equal_v2(lstofnums: List[int]) -> bool:
    if len(lstofnums) < 1:
        return False
    for index in range(len(lstofnums) - 1):
        if lstofnums[index] != lstofnums[index + 1]:
            return False
    return True

class TestAppMethods(unittest.TestCase):
    def testing_all_equal_v1(self):
        self.assertEqual(all_equal_v1([]), False)
        self.assertEqual(all_equal_v1([1, 2, 3]), False)
        self.assertEqual(all_equal_v1([1, 1, 1, 1]), True)
        self.assertEqual(all_equal_v1([1, 1, 1, 2]), False)
    
    def testing_all_equal_v2(self):
        self.assertEqual(all_equal_v2([]), False)
        self.assertEqual(all_equal_v2([1, 2, 3]), False)
        self.assertEqual(all_equal_v2([1, 1, 1, 1]), True)
        self.assertEqual(all_equal_v2([1, 1, 1, 2]), False)
        
        
        
if __name__ == '__main__':
    unittest.main()
    