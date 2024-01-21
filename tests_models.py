from unittest import TestCase
from models import Conversion

class ConversionTestCase(TestCase):

    def test_verify_cur_hp(self):
        test_conv = Conversion('CAD','CAD', 10)
        self.assertEqual(test_conv.verify_cur()[0], True)

    def test_verify_curto_nhp(self):
        test_conv2 = Conversion('ZZZ','CAD', 10)
        self.assertEqual(test_conv2.verify_cur()[0], False)

    def test_verify_curfrom_nhp(self):
        test_conv3 = Conversion('CAD','ZZZ', 10)
        self.assertEqual(test_conv3.verify_cur()[0], False)

    def test_verify_amt(self):
        test_conv4 = Conversion('CAD','USD', 'abc')
        self.assertEqual(test_conv4.verify_amt(), False)