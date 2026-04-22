"""sample tests"""

from django.test import SimpleTestCase
from app import calc


class calcTests(SimpleTestCase):

    def test_add_numbers(self):
        """ test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_subtract_number(self):
        """test the subtract function"""
        res=calc.subtract(10, 5)
        self.assertEqual(res, 5)
