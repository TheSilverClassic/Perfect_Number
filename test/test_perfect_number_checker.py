import unittest
from src.perfect_number_checker import add, perfect_number_check, calculate_factors_of_number

class CanaryTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_add(self):
        self.assertEqual(add(1, 1), 2)

class PerfectNumberChecker(unittest.TestCase):

    def test_calculate_factors_of_number_6(self):
        self.assertEqual(calculate_factors_of_number(6), [1, 2, 3])

    def test_calculate_factors_of_number_28(self):
        self.assertEqual(calculate_factors_of_number(28), [1, 2, 4, 7, 14])

    def test_calculate_factors_of_number_496(self):
        self.assertEqual(calculate_factors_of_number(496), [1, 2, 4, 8, 16, 31, 62, 124, 248])

    def test_calculate_factors_of_number_500(self):
        self.assertEqual(calculate_factors_of_number(500), [1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250])

    def test_perfect_number_check_6_true(self):
        self.assertTrue(perfect_number_check(6))

    def test_perfect_number_check_28_true(self):
        self.assertTrue(perfect_number_check(28))

    def test_perfect_number_check_496_true(self):
        self.assertTrue(perfect_number_check(496))

    def test_perfect_number_check_500_false(self):
        self.assertFalse(perfect_number_check(500))
