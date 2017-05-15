from unittest import TestCase

from assingment.valuation_service.aggregate import get_key, create_dict_matching_products, compare_products_to_matches, \
    get_top_low_for_match
from assingment.valuation_service.models.matches import Matches
from assingment.valuation_service.models.product import Product


class TestAggregate(TestCase):
    def test_create_dict_matching_products(self):
        """Tests for create dict matching products"""
        self.assertIsInstance(create_dict_matching_products([4, 5]), dict)
        self.assertEqual(create_dict_matching_products([4, 5]), {1: [], 2: [], 3: [], 4: [], 5: []})

    def test_compare_products_to_matches(self):
        """Tests for create dict matching products"""
        products = [Product('1', '100', 'GBP', '3', '5')]
        matches = [Matches('5', '2'), Matches('1', '2')]
        self.assertIsInstance(compare_products_to_matches(products, matches, [1, 4, 6, 5]), dict)

    def test_get_top_low_for_match(self):
        """Tests for create dict matching products"""
        self.assertIsInstance(get_top_low_for_match({}), list)
