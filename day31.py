''' Solution to task from https://www.instagram.com/p/CbwenENg-G9/ '''

from email.policy import default
from typing import Optional
import unittest

# one-liner
def count_ones_v1(num: int) -> int:
    return sum([str(x).count('1') for x in range(num + 1)])

# second solution
def count_ones_v2(num: int) -> int:
    ones, power, default, prev_rest = 0, 0, 0, 0
    while num > 0:
        print(num, ones, power, default, prev_rest)
        if num % 10 > 1:
            ones += 10 ** power
        elif num % 10 == 1:
            ones += 1 + prev_rest * 10 ** (power - 1)
        default += 10 ** power
        power += 1
        prev_rest = num % 10
        num //= 10
    
    print(num, ones, power, default, prev_rest)
    return ones
    

class TestAppMethods(unittest.TestCase):
    
    def testing_count_ones_v1(self):
        self.assertEqual(count_ones_v1(1), 1)
        self.assertEqual(count_ones_v1(10), 2)
        self.assertEqual(count_ones_v1(19), 12)
        self.assertEqual(count_ones_v1(100), 21)
        
    def testing_count_ones_v2(self):
        self.assertEqual(count_ones_v2(1), 1)
        self.assertEqual(count_ones_v2(10), 2)
        self.assertEqual(count_ones_v2(19), 12)
        self.assertEqual(count_ones_v2(100), 21)
        
        
if __name__ == '__main__':
    unittest.main()
    