''' Solution to task from https://www.instagram.com/p/CbhI_-rgVXa/ '''


from typing import List
import unittest


def fibonacci(num: int) -> List[int]:
    if num < 0:
        return -1
    if num == 0:
        return [0]
    fiblst = [0, 1]
    for _ in range(2, num + 1):
        fiblst.append(fiblst[-2] + fiblst[-1])
    return fiblst
    



class TestAppMethods(unittest.TestCase):
    def testing_fibonacci(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci(1), [0, 1])
        self.assertEqual(fibonacci(2), [0, 1, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1, 2])
        
        
        
if __name__ == '__main__':
    unittest.main()
    