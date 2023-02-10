import unittest

from lesson_20_hw_20.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def test_zero(self):
        f = Fibonacci()
        self.assertEqual(f(0), 0)

    def test_1(self):
        f = Fibonacci()
        self.assertEqual(f(1), 1)

    def test_3(self):
        f = Fibonacci()
        self.assertEqual(f(10), 55)

    def test_negative(self):
        f = Fibonacci()
        self.assertRaises(ValueError, f, -1)

    def test_string(self):
        f = Fibonacci()
        self.assertRaises(ValueError, f, "1")

    def test_float(self):
        f = Fibonacci()
        self.assertRaises(ValueError, f, 1.5)


if __name__ == '__main__':
    unittest.main()
