import unittest
from src.perfect_numbers_up_to_limit import perfect_numbers_up_to_limit

class PerfectNumberUpToLimit(unittest.TestCase):

    def test_perfect_number_up_to_limit_check_list(self):
        function_result = perfect_numbers_up_to_limit(6)
        self.assertTrue(isinstance(function_result, list))

    def test_perfect_number_up_to_limit_1(self):
        self.assertEqual(perfect_numbers_up_to_limit(1), [])

    def test_perfect_number_up_to_limit_6(self):
        self.assertEqual(perfect_numbers_up_to_limit(6), [6])

    def test_perfect_number_up_to_limit_496(self):
        self.assertEqual(perfect_numbers_up_to_limit(496), [6, 28, 496])

    def test_perfect_number_up_to_limit_500(self):
        self.assertEqual(perfect_numbers_up_to_limit(500), [6, 28, 496])
