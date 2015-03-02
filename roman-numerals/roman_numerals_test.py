from collections import OrderedDict
import unittest

import roman


class RomanTest(unittest.TestCase):
    numerals = OrderedDict(sorted({
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        9: 'IX',
        27: 'XXVII',
        48: 'XLVIII',
        59: 'LIX',
        93: 'XCIII',
        141: 'CXLI',
        163: 'CLXIII',
        402: 'CDII',
        575: 'DLXXV',
        911: 'CMXI',
        1024: 'MXXIV',
        3000: 'MMM',
    }.items(), key=lambda kv: kv[0]))

    def test_numerals(self):
        for arabic, numeral in self.numerals.items():
            self.assertEqual(numeral, roman.numeral(arabic))
            print '{0} / {1} : OK'.format(arabic, numeral)

if __name__ == '__main__':
    unittest.main()
