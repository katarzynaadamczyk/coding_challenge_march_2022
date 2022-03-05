''' Solution to task from https://www.instagram.com/p/CarGouiAN8c/ '''


import pandas as pd
import unittest


def gerund_infinitive1(word):
    return 'to ' + word[:-3] if word[-3::] == 'ing' else 'To nie jest rzeczownik odsłowny'


def gerund_infinitive2(word, listofverbs):
    if not(len(word) < 4 or word[-3::] != 'ing'):        
        verb = word[:-3]
        if verb in listofverbs:
            return 'to ' + verb
        if (verb + 'e') in listofverbs:
            return 'to ' + verb + 'e'
        if verb[:-1] in listofverbs:
            return 'to ' + verb[:-1] 
    return 'To nie jest rzeczownik odsłowny'


class TestAppMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(gerund_infinitive1('doing'), 'to do')
        self.assertEqual(gerund_infinitive1('having'), 'to hav')
        self.assertEqual(gerund_infinitive1('habit'), 'To nie jest rzeczownik odsłowny')
    
    def test2(self):
        verblist = pd.read_csv('day4data.csv', sep=',')
        verblist = list(verblist['verb'])
        self.assertEqual(gerund_infinitive2('doing', verblist), 'to do')
        self.assertEqual(gerund_infinitive2('having', verblist), 'to have')
        self.assertEqual(gerund_infinitive2('omitting', verblist), 'to omit')
        self.assertEqual(gerund_infinitive2('habit', verblist), 'To nie jest rzeczownik odsłowny')


if __name__ == '__main__':
    unittest.main()
    