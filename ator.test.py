import unittest

from ator import arabic_to_roman


class TestArabicNumberToRoman(unittest.TestCase):

    def test_convert_1(self):
        self.assertEqual(arabic_to_roman(1), 'I')

    def test_convert_2(self):
        self.assertEqual(arabic_to_roman(2), 'II')

    def test_convert_3(self):
        self.assertEqual(arabic_to_roman(3), 'III')

    def test_convert_4(self):
        self.assertEqual(arabic_to_roman(4), 'IV')

    def test_convert_5(self):
        self.assertEqual(arabic_to_roman(5), 'V')

    def test_numbers_up_to_8(self):
        pairs = [(6, 'VI'), (7, 'VII'), (8, 'VIII')]
        for arabic, roman in pairs:
            self.assertEqual(arabic_to_roman(arabic), roman)

    def test_convert_9(self):
        self.assertEqual(arabic_to_roman(9), 'IX')

    def test_convert_10(self):
        self.assertEqual(arabic_to_roman(10), 'X')

    def test_numbers_up_to_13(self):
        pairs = [('XI', 11), ('XII', 12), ('XIII', 13)]
        for roman, arabic in pairs:
            self.assertEqual(arabic_to_roman(arabic), roman)


if __name__ == '__main__':
    unittest.main()