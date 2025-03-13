import unittest
from add_numbers import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(2, -3), -1)

if __name__ == '__main__':
    unittest.main()
