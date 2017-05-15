from unittest import TestCase
from planety.valuation_service.models.product import Product


class TestProduct(TestCase):
    def test_get_key(self):
        product = Product('1', '2', '3', '4', '5')
        self.assertIsNone(product.get_key(), None)
