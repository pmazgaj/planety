from unittest import TestCase
from planety.valuation_service.calculations import get_parsed_column, get_sum_for_column, parse_num_to_int
from planety.valuation_service.calculations import get_average_value_for_column


class TestCalculations(TestCase):
    def test_get_parsed_column(self):
        self.assertListEqual(get_parsed_column(['3', '4', '5']), [3, 4, 5])

    def test_get_average_value_for_column(self):
        self.assertEqual(get_average_value_for_column(['4', '5']), 4.5)
        self.assertIsInstance(get_average_value_for_column(['4', '5']), float)

    def test_get_sum_for_column(self):
        self.assertNotEqual(get_sum_for_column([1, 2.0, 3.0]), int)

    def test_parse_num(self):
        self.assertNotEqual(parse_num_to_int('x'), 1)
        self.assertIsInstance(parse_num_to_int('dummy'), float)
