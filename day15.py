''' Solution to task from https://www.instagram.com/p/CbHbC_7gI_u/ '''


import string
import unittest

# one dot after each sign except for the last one
def add_dots_v1(word: string) -> string:
    return '.'.join(word)

# one dot between alphanumeric signs in a sentence 
def add_dots_v2(word: string) -> string:
    return ''.join([word[index] + '.' if word[index:index+2].isalpha() else word[index] for index in range(len(word) - 1)]) + word[-1]


class TestAppMethods(unittest.TestCase):
    def testing_add_dots_v1(self):
        self.assertEqual(add_dots_v1('test'), 't.e.s.t')
        self.assertEqual(add_dots_v1('test case'), 't.e.s.t. .c.a.s.e')
        
    def testing_add_dots_v2(self):
        self.assertEqual(add_dots_v2('test'), 't.e.s.t')
        self.assertEqual(add_dots_v2('test case'), 't.e.s.t c.a.s.e')
        
if __name__ == '__main__':
    unittest.main()
    