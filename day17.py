''' Solution to task from https://www.instagram.com/p/CbMjijXggtN/ '''

import numpy as np
import unittest

# recursion version
def calculate_factorial_v1(num: int) -> int:
    if num < 1:
        return 0
    if num == 1:
        return 1
    return num * calculate_factorial_v1(num - 1)

# loop version
def calculate_factorial_v2(num: int) -> int:
    if num < 1:
        return 0
    prod = 1
    for x in range(1, num + 1):
        prod *= x
    return prod

# array version
def calculate_factorial_v3(num: int) -> int:
    if num < 1:
        return 0
    return np.prod([x for x in range(1, num + 1)])


class TestAppMethods(unittest.TestCase):
    def testing_calculate_factorial_v1(self):
        self.assertEqual(calculate_factorial_v1(5), 5 * 4 * 3 * 2)
        self.assertEqual(calculate_factorial_v1(1), 1)
        self.assertEqual(calculate_factorial_v1(-10), 0)
    
    def testing_calculate_factorial_v2(self):
        self.assertEqual(calculate_factorial_v2(5), 5 * 4 * 3 * 2)
        self.assertEqual(calculate_factorial_v2(1), 1)
        self.assertEqual(calculate_factorial_v2(-10), 0)
        
    def testing_calculate_factorial_v3(self):
        self.assertEqual(calculate_factorial_v3(5), 5 * 4 * 3 * 2)
        self.assertEqual(calculate_factorial_v3(1), 1)
        self.assertEqual(calculate_factorial_v3(-10), 0)
        
        
if __name__ == '__main__':
    unittest.main()
    