from modules.module1.arithmetic import add, subtract, divide, multiply


import unittest


class TestArithmeticAdd(unittest.TestCase):
    def test_add_positive(self):
        num1 = 1
        num2 = 2
        self.assertEqual(3, add(num1, num2))

    def test_add_negative(self):
        num1 = -1
        num2 = -2
        self.assertEqual(-3, add(num1, num2))

    def test_add_mixed(self):
        num1 = 1
        num2 = -2
        self.assertEqual(-1, add(num1, num2))


class TestArithmeticSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        num1 = 1
        num2 = 2
        self.assertEqual(-1, subtract(num1, num2))

    def test_subtract_negative(self):
        num1 = -1
        num2 = -2
        self.assertEqual(1, subtract(num1, num2))

    def test_subtract_mixed(self):
        num1 = 1
        num2 = -2
        self.assertEqual(3, subtract(num1, num2))
        num1 = 1
        num2 = -2
        self.assertEqual(-3, subtract(num2, num1))


class TestArithmeticMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        num1 = 1
        num2 = 2
        self.assertEqual(2, multiply(num1, num2))

    def test_multiply_negative(self):
        num1 = -1
        num2 = -2
        self.assertEqual(2, multiply(num1, num2))

    def test_multiply_mixed(self):
        num1 = 1
        num2 = -2
        self.assertEqual(-2, multiply(num1, num2))

    def test_multiply_zero(self):
        num1 = 1
        num2 = 0
        self.assertEqual(0, multiply(num1, num2))


class TestArithmeticDivide(unittest.TestCase):
    def test_divide_positive(self):
        num1 = 1
        num2 = 2
        self.assertAlmostEqual(0.5, divide(num1, num2))

    def test_divide_negative(self):
        num1 = -1
        num2 = -2
        self.assertAlmostEqual(0.5, divide(num1, num2))

    def test_divide_mixed(self):
        num1 = 1
        num2 = -2
        self.assertAlmostEqual(-0.5, divide(num1, num2))

    def test_divide_by_zero(self):
        num1 = 1
        num2 = 0
        with self.assertRaises(ValueError) as ve:
            _ = divide(num1, num2)
        self.assertEqual("Cannot divide: Second number cannot be 0", ve.exception.args[0])

    def test_divide_zero(self):
        num1 = 0
        num2 = 1
        self.assertEqual(0, divide(num1, num2))
