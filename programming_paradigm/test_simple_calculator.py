import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(3, -2), 1)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(6, 1), 5)
        self.assertEqual(self.calc.subtract(-8, 2), -6)
        self.assertEqual(self.calc.subtract(-3, -3), -6)
        self.assertEqual(self.calc.subtract(4, -2), 6)
    
    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
        self.assertEqual(self.calc.multiply(1, -3), -3)
        self.assertEqual(self.calc.multiply(-4, 2), -8)

    def test_division(self):
        """Test the division of numbers"""
        self.assertEqual(self.calc.divide(0, 10), 0)
        self.assertEqual(self.calc.divide(12, 4), 3)
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(-4, -2), -2)
        self.assertEqual(self.calc.divide(-15, 3), -5)
        self.assertEqual(self.calc.divide(6, -2), -3)
if __name__ == "main":
    unittest.main()
# Remember to write additional test methods for subtract, multiply, and divide.