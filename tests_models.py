from unittest import TestCase
from models import Conversion
from app import app

app.config['TESTING'] = True

class ConversionTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual('/forex_form', response.headers['Location'])

    def test_submit_pass(self):
        response = self.app.post('/submit_form', data = {
            'convert_from': 'USD',
            'convert_to': 'CAD',
            'amount': '100'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('<display id="result_display">The Result is', response.data.decode('utf-8'))

    def test_submit_fail_curfrom(self):
        response = self.app.post('/submit_form', data = {
            'convert_from': 'blahblah',
            'convert_to': 'CAD',
            'amount': '100'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p class="flashMsg">BLAHBLAH is not a valid FROM currency</p>', response.data.decode('utf-8'))

    def test_submit_fail_curto(self):
        response = self.app.post('/submit_form', data = {
            'convert_from': 'CAD',
            'convert_to': 'blahblah',
            'amount': '100'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p class="flashMsg">BLAHBLAH is not a valid TO currency</p>', response.data.decode('utf-8'))

    def test_submit_fail_amt(self):
        response = self.app.post('/submit_form', data = {
            'convert_from': 'USD',
            'convert_to': 'CAD',
            'amount': 'abc'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p class="flashMsg">Amount must be a numerical value.</p>', response.data.decode('utf-8'))

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