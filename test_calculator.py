import unittest
from calculator import add #import the function that going to be tested

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

#This let's you run the test by just running this script

if __name__ == '__main__':
    unittest.main()
