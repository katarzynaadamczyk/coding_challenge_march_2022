''' Solution to task from https://www.instagram.com/p/CbrU6QfASzs/ '''


import unittest

def additive_persistence(num: int) -> int:
    retval = 0
    while abs(num) > 9:
        retval += 1
        num = sum([int(x) for x in str(abs(num))])
    return retval



class TestAppMethods(unittest.TestCase):
    def testing_additive_persistence(self):
        self.assertEqual(additive_persistence(199), 3)
        self.assertEqual(additive_persistence(-199), 3)
        self.assertEqual(additive_persistence(1), 0)
        self.assertEqual(additive_persistence(10), 1)
        
        
        
if __name__ == '__main__':
    unittest.main()
    