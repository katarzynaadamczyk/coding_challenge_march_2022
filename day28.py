''' Solution to task from https://www.instagram.com/p/Cbow5D-Aseh/ '''


import unittest

# one-liner
def digit_adder_v1(num: int) -> int:
    return (-1 if num < 0 else 1 ) * \
        int(''.join([str(int(x) + 1) for x in list(str(num))]))
    
# second solution
def digit_adder_v2(num: int) -> int:
    if num < 0:
        retval = '-'
        num *= -1
    else:
        retval = ''
    for digit in str(num):
        retval += str(int(digit) + 1)
    return int(retval)



class TestAppMethods(unittest.TestCase):
    def testing_digit_adder_v1(self):
        self.assertEqual(digit_adder_v1(998), 10109)
        self.assertEqual(digit_adder_v1(10109), 212110)
        
    
    def testing_digit_adder_v2(self):
        self.assertEqual(digit_adder_v2(998), 10109)
        self.assertEqual(digit_adder_v2(10109), 212110)
        
        
if __name__ == '__main__':
    unittest.main()
    