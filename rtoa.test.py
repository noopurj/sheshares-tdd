import unittest

from rtoa import roman_to_arabic


class TestRomanToNumber(unittest.TestCase):

    def test_convert_1(self):
        self.assertEqual(roman_to_arabic('I'), 1)

    def test_convert_2(self):
        self.assertEqual(roman_to_arabic('II'), 2)

    def test_convert_3(self):
        self.assertEqual(roman_to_arabic('III'), 3)

    def test_convert_4(self):
        self.assertEqual(roman_to_arabic('IV'), 4)

    def test_convert_5(self):
        self.assertEqual(roman_to_arabic('V'), 5)

    def test_numbers_up_to_8(self):
        pairs = [('VI', 6), ('VII', 7), ('VIII', 8)]
        for roman, arabic in pairs:
            self.assertEqual(roman_to_arabic(roman), arabic)

    def test_convert_9(self):
        self.assertEqual(roman_to_arabic('IX'), 9)

    def test_convert_10(self):
        self.assertEqual(roman_to_arabic('X'), 10)

    def test_numbers_up_to_13(self):
        pairs = [('XI', 11), ('XII', 12), ('XIII', 13)]
        for roman, arabic in pairs:
            self.assertEqual(roman_to_arabic(roman), arabic)

    def test_convert_14(self):
        self.assertEqual(roman_to_arabic('XIV'), 14)

    def test_convert_15(self):
        self.assertEqual(roman_to_arabic('XV'), 15)

    def test_numbers_up_to_20(self):
        pairs = [('XVI', 16), ('XVII', 17), ('XVIII', 18), ('XIX', 19), ('XX', 20)]
        for roman, arabic in pairs:
            self.assertEqual(roman_to_arabic(roman), arabic)

    def test_convert_25(self):
        self.assertEqual(roman_to_arabic('XXV'), 25)

    def test_convert_40(self):
        self.assertEqual(roman_to_arabic('XL'), 40)

    def test_convert_3724(self):
        self.assertEqual(roman_to_arabic('MMMDCCXXIV'), 3724)


if __name__ == '__main__':
    unittest.main()
