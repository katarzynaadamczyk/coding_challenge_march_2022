''' Solution to task from https://www.instagram.com/p/Cbek7shAwHa/ '''


from typing import List
import unittest


def is_geometric(nums: List[int]) -> bool:
    if len(nums) > 1:
        q = nums[1] / nums[0]
        for index in range(1, len(nums) - 1):
            if nums[index + 1] / nums[index] != q:
                return False
        return True
    return False



class TestAppMethods(unittest.TestCase):
    def testing_is_geometric(self):
        self.assertEqual(is_geometric([1, 2, 4, 8]), True)
        self.assertEqual(is_geometric([1, 2, 4, 9]), False)
        self.assertEqual(is_geometric([1]), False)
        self.assertEqual(is_geometric([1, 3, 4, 9]), False)
        
        
        
if __name__ == '__main__':
    unittest.main()
    