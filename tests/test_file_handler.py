from unittest import TestCase
from assingment.valuation_service.file_handler import get_all_values_for_column, fill_product_object, fill_matches_object, \
    fill_currency_object
from assingment.valuation_service.file_handler import parse_csv
from assingment.valuation_service.file_handler import parse_reader
from assingment.valuation_service.file_handler import save_csv_to_file


class TestFileHandler(TestCase):
    def test_get_all_values_for_column(self):
        """tests for get_all_values"""
        self.assertEqual(get_all_values_for_column(parse_csv('matchings.csv'), 'matching_id'), ['1', '2', '3'])

    def test_parse_reader(self):
        """tests for parse_reader"""
        self.assertIsInstance(parse_reader(parse_csv('matchings.csv')), list)

    def test_parse_csv(self):
        """tests for parse_csv"""
        self.assertIsInstance(parse_csv('matchings.csv'), list)

    def test_save_csv_to_file(self):
        """test for save csv"""
        self.assertIsNone(save_csv_to_file())

    def test_fill_product_object(self):
        """tests for filling product list with Product objects"""
        self.assertIsInstance(fill_product_object(parse_csv('data.csv')), list)

    def test_fill_matches_object(self):
        """tests for filling product list with Product objects"""
        self.assertIsInstance(fill_matches_object(parse_csv('matchings.csv')), list)

    def test_fill_currency_object(self):
        """tests for filling product list with Product objects"""
        self.assertIsInstance(fill_currency_object(parse_csv('currencies.csv')), list)
