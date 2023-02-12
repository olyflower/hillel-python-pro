import unittest

from lesson_20_hw_20.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.f = Fibonacci()

    def test_zero(self):
        self.assertEqual(self.f(0), 0)

    def test_1(self):
        self.assertEqual(self.f(1), 1)

    def test_ordinary_number(self):
        self.assertEqual(self.f(10), 55)

    def test_big_number_100(self):
        self.assertEqual(self.f(100), 354224848179261915075)

    def test_big_number_400(self):
        self.assertEqual(self.f(400), 176023680645013966468226945392411250770384383304492191886725992896575345044216019675)

    def test_negative(self):
        self.assertRaises(ValueError, self.f, -1)

    def test_string(self):
        self.assertRaises(ValueError, self.f, "1")

    def test_float(self):
        self.assertRaises(ValueError, self.f, 1.5)


if __name__ == '__main__':
    unittest.main()
