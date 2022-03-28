''' Solution to task from https://www.instagram.com/p/Cbow5D-Aseh/ '''


import unittest


def digit_adder(num: int) -> int:
    return -1 if num < 0 else \
        int(''.join([str(int(x) + 1) for x in list(str(num))]))
    



class TestAppMethods(unittest.TestCase):
    def testing_digit_adder(self):
        self.assertEqual(digit_adder(998), 10109)
        self.assertEqual(digit_adder(10109), 212110)
        
        
        
if __name__ == '__main__':
    unittest.main()
    