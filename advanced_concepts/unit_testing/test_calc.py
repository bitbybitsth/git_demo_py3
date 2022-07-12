import unittest
from calc import add, sub, div, mul, MultipliedByZero


class TestTuesday(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(5, -10), -5)
        self.assertNotEqual(add(10, 20), 31)
        self.assertFalse(add(0, 0))
        self.assertTrue(add(5,5))
        self.assertIsNotNone(add(5, 6))

    def test_sub(self):
        self.assertEqual(sub(10,5),5)
        self.assertEqual(sub(-10, 5), -15)
        self.assertEqual(sub(10, -5), 15)
        self.assertEqual(sub(-10, -5), -5)

    def test_div(self):
        self.assertRaises((ZeroDivisionError,), div, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            # pre operation
            div(10, 0)


        self.assertEqual(div(10, 1), 10)
        self.assertRaises((ZeroDivisionError, TypeError), div, 10, "0")

    def test_mul(self):
        self.assertEqual(mul(10,20), 200)
        self.assertEqual(mul(-10, 20), -200)
        self.assertEqual(mul(-10, -20), 200)
        self.assertRaises((MultipliedByZero,), mul, 0, 9)
        self.assertRaises((MultipliedByZero,), mul, 9, 0)

    def test_add_new(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(5, -10), -5)
        self.assertNotEqual(add(10, 20), 31)
        self.assertFalse(add(0, 0))
        self.assertTrue(add(5,5))
        self.assertIsNotNone(add(5, 6))

if __name__ == '__main__':
    unittest.main()