import unittest
from .... import challenges as d


class TestHasTwoNumbers(unittest.TestCase):
    def test_has_two_numbers_empty_list(self):
        self.assertFalse(d.has_two_numbers([], 10))

    def test_has_two_numbers_not_found(self):
        self.assertFalse(has_two_numbers([1, 2, 3, 4], 10))

    def test_has_two_numbers_found(self):
        self.assertTrue(has_two_numbers([1, 2, 3, 4], 7))

    def test_has_two_numbers_multiple_found(self):
        self.assertTrue(has_two_numbers([1, 2, 3, 4, 5], 7))
        self.assertTrue(has_two_numbers([1, 2, 3, 4, 5], 8))

    def test_has_two_numbers_positive(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 10
        self.assertTrue(has_two_numbers(l, k))

    def test_has_two_numbers_negative(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = -15
        self.assertFalse(has_two_numbers(l, k))


if __name__ == '__main__':
    unittest.main()
