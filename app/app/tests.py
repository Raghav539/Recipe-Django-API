"""
Tests for calculator functions
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_Add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(3, 8)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers together."""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)

    def test_multiply_numbers(self):
        """Test multiplying numbers together."""
        res = calc.multiply(4, 7)

        self.assertEqual(res, 28)

    def test_divide_numbers(self):
        """Test dividing numbers together."""
        res = calc.divide(10, 2)

        self.assertEqual(res, 5)