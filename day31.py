''' Solution to task from https://www.instagram.com/p/CbwenENg-G9/ '''

import time
from typing import Optional
import unittest

def measuretime(func):
    def wrapper(*args, **kwargs):
        starttime = time.perf_counter_ns()
        ret = func(*args, **kwargs)
        endtime = time.perf_counter_ns()
        print(f'Time needed: {endtime - starttime} ns')
        return ret
    return wrapper


# one-liner, o(n)
@measuretime
def count_ones_v1(num: int) -> int:
    return sum([str(x).count('1') for x in range(num + 1)])

# second solution, o(log(n)) 
@measuretime
def count_ones_v2(num: int) -> int:
    original_num, power, ones, lst_defaults = num, 0, 0, [0]
    while num > 0:
        lst_defaults.append(10 ** power + 10 * lst_defaults[-1])
        num //= 10
        power += 1
    for index in range(len(lst_defaults) - 1, -1, -1):
        ones += original_num // 10 ** index * lst_defaults[index]
        if original_num // 10 ** index == 1:
            ones += 1 + original_num % 10 ** index
        elif original_num // 10 ** index > 1:
            ones += 10 ** index
        original_num -= original_num // 10 ** index * 10 ** index
    return ones
    
# third solution, one loop, o(log(n))
@measuretime
def count_ones_v3(num: int) -> int:
    original_num, power, ones, default_value = num, 0, 0, 0
    while num > 0:
        ones += num % 10 * default_value
        if num % 10 == 1:
            ones += 1 + original_num % 10 ** power
        elif num % 10 > 1:
            ones += 10 ** power
        default_value = 10 ** power + 10 * default_value
        num //= 10
        power += 1
    return ones

class TestAppMethods(unittest.TestCase):
    
    def testing_count_ones_v1(self):
        self.assertEqual(count_ones_v1(1), 1)
        self.assertEqual(count_ones_v1(10), 2)
        self.assertEqual(count_ones_v1(19), 12)
        self.assertEqual(count_ones_v1(100), 21)
        
    def testing_count_ones_v2(self):
        self.assertEqual(count_ones_v2(100), 21)
        self.assertEqual(count_ones_v2(19), 12)
        self.assertEqual(count_ones_v2(1), 1)
        self.assertEqual(count_ones_v2(10), 2)
        self.assertEqual(count_ones_v2(1020584), count_ones_v1(1020584))

    def testing_count_ones_v3(self):
        self.assertEqual(count_ones_v3(100), 21)
        self.assertEqual(count_ones_v3(19), 12)
        self.assertEqual(count_ones_v3(1), 1)
        self.assertEqual(count_ones_v3(10), 2)
        self.assertEqual(count_ones_v3(1020584), count_ones_v1(1020584))


def main():
    print('v1:', count_ones_v1(1020584))
    print('v2:', count_ones_v2(1020584))
    print('v3:', count_ones_v3(1020584))
    
        
if __name__ == '__main__':
    #unittest.main()
    main()
    
    
    