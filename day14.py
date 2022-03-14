''' Solution to task from https://www.instagram.com/p/CbE5Kl3AzJN/ '''


from typing import List
import unittest

# one-liner
def largest_difference_v1(lst: List[int]) -> int:
    return max(lst) - min(lst)


# not a one-line solution
def largest_difference_v2(lst: List[int]) -> int:
    max_num, min_num = lst[0], lst[0]
    for index in range(1, len(lst)):
        if lst[index] > max_num:
            max_num = lst[index]
        elif lst[index] < min_num:
            min_num = lst[index]
    return max_num - min_num


class TestAppMethods(unittest.TestCase):
    def testing_largest_difference_v1(self):
        self.assertEqual(largest_difference_v1([1, 2, 3, 4, 5, 6]), 5)
        self.assertEqual(largest_difference_v1([1, 1, 1, 1, 1]), 0)

    def testing_largest_difference_v1(self):
        self.assertEqual(largest_difference_v2([1, 2, 3, 4, 5, 6]), 5)
        self.assertEqual(largest_difference_v2([1, 1, 1, 1, 1]), 0)
        
        
if __name__ == '__main__':
    unittest.main()
    