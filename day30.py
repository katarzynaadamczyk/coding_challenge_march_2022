''' Solution to task from https://www.instagram.com/p/Cbt6udegxjM/ '''


from tokenize import String
import unittest


class RomanNumerals:
    
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def from_roman(self, roman_num: String) -> int:
        if len(roman_num):
            num = self.roman_dict[roman_num[-1]]
            for i in range(0, len(roman_num) - 1):
                if self.roman_dict[roman_num[i + 1]] > self.roman_dict[roman_num[i]]:
                    num -= self.roman_dict[roman_num[i]]
                else:
                    num += self.roman_dict[roman_num[i]]
            return num
        return 0

    def rom_num_compare(self, rom_num_1: String, rom_num_2: String) -> bool:
        return self.from_roman(rom_num_1) < self.from_roman(rom_num_2)
        

class TestAppMethods(unittest.TestCase):
    
    def testing_rom_num_compare(self):
        numerals = RomanNumerals()
        self.assertEqual(numerals.rom_num_compare('X', 'XV'), True)
        self.assertEqual(numerals.rom_num_compare('L', 'XV'), False)
        self.assertEqual(numerals.rom_num_compare('MDCLXV', 'MDCLXVI'), True)
        
        
if __name__ == '__main__':
    unittest.main()
    