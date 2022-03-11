''' Solution to task from https://www.instagram.com/p/Ca9HMj7gjDh/ '''


import string
import unittest

# oneliner, case-sensitive
def is_anagram_v1_1(word1: string, word2: string) -> bool:
    return word1.isalpha() and sorted(word1) == sorted(word2) and word1 != word2


# dict-version, case-sensitive
def is_anagram_v1_2(word1: string, word2: string) -> bool:
    if word1.isalpha() and word2.isalpha() and word1 != word2:
        def get_letters_dictionary(word: string) -> dict:
            letters_dict = {}
            for letter in word:
                letters_dict.setdefault(letter, 0)
                letters_dict[letter] += 1
            return letters_dict
        letters_dict_1 = get_letters_dictionary(word1)
        letters_dict_2 = get_letters_dictionary(word2)
        for letter, letter_quantity in letters_dict_1.items():
            if letter in letters_dict_2.keys() and letters_dict_2[letter] == letter_quantity:
                del letters_dict_2[letter]
        if len(letters_dict_2.keys()) == 0:
            return True
    return False
    

# oneliner, case-insensitive
def is_anagram_v2_1(word1: string, word2: string) -> bool:
    return word1.isalpha() and sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()


class TestAppMethods(unittest.TestCase):
    def testing_is_anagram_v1_1(self):
        self.assertEqual(is_anagram_v1_1('kasia', 'asiak'), True)
        self.assertEqual(is_anagram_v1_1('kasia', 'asiaK'), False)

    def testing_is_anagram_v1_2(self):
        self.assertEqual(is_anagram_v1_2('kasia', 'asiak'), True)
        self.assertEqual(is_anagram_v1_2('kasia', 'asiaK'), False)
        
    def testing_is_anagram_v2_1(self):
        self.assertEqual(is_anagram_v2_1('kasia', 'asiak'), True)
        self.assertEqual(is_anagram_v2_1('kasia', 'asiaK'), True)
        self.assertEqual(is_anagram_v2_1('kasia', 'asiaKi'), False)

if __name__ == '__main__':
    unittest.main()
    