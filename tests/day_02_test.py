import unittest
from challenges.day_02 import new_multiply_array


class TestNewMultiplyArray(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(new_multiply_array([]), [])

    def test_one_element(self):
        self.assertEqual(new_multiply_array([2]), [])

    def test_multiple_elements(self):
        self.assertEqual(new_multiply_array([2, 3, 4]), [12, 8, 6])

    def test_negative_elements(self):
        self.assertEqual(new_multiply_array([-2, 3, 4]), [12, -8, -6])

    def test_zero_element(self):
        with self.assertRaises(ZeroDivisionError):
            new_multiply_array([0, 2, 3])


if __name__ == '__main__':
    unittest.main()
