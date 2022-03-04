''' Solution to task from https://www.instagram.com/p/CarGouiAN8c/ '''

import unittest

def gerund_infinitive(word):
    return 'to ' + word[:-3] if word[-3::] == 'ing' else 'To nie jest rzeczownik odsłowny'


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(gerund_infinitive('doing'), 'to do')
        self.assertEqual(gerund_infinitive('having'), 'to hav')
        self.assertEqual(gerund_infinitive('habit'), 'To nie jest rzeczownik odsłowny')


if __name__ == '__main__':
    unittest.main()
    