''' Solution to task from https://www.instagram.com/p/CbW2AxFgAjL/ '''

from typing import List
import unittest


def move_zero(lstofnums: List[int]) -> List[int]:
    changes_needed = []
    for index in range(len(lstofnums) - 1, -1, -1):
        if lstofnums[index] == 0:
            changes_needed.append(index)
            lstofnums.append(0)
    for index in changes_needed:
        del lstofnums[index]
    return lstofnums

# one-liner
def move_zero_v2(lstofnums: List[int]) -> List[int]:
    return sorted(lstofnums, key=lambda x: x==0)

class TestAppMethods(unittest.TestCase):
    def testing_move_zero(self):
        self.assertEqual(move_zero([]), [])
        self.assertEqual(move_zero([0, 0, 0, 11]), [11, 0, 0, 0])
        self.assertEqual(move_zero([1, 0, 2]), [1, 2, 0])
        self.assertEqual(move_zero([2, 0, 1]), [2, 1, 0])
        self.assertEqual(move_zero([0, 2, 0, 1]), [2, 1, 0, 0])
        self.assertEqual(move_zero([2, 1, 0]), [2, 1, 0])
        
    def testing_move_zero_v2(self):
        self.assertEqual(move_zero_v2([]), [])
        self.assertEqual(move_zero_v2([0, 0, 0, 11]), [11, 0, 0, 0])
        self.assertEqual(move_zero_v2([1, 0, 2]), [1, 2, 0])
        self.assertEqual(move_zero_v2([2, 0, 1]), [2, 1, 0])
        self.assertEqual(move_zero_v2([2, 1, 0]), [2, 1, 0])
        
        
if __name__ == '__main__':
    unittest.main()
    