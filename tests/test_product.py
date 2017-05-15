from unittest import TestCase


class TestProduct(TestCase):
    def test_get_key(self):
        from planety.valuation_service.models.product import Product
        product = Product('1', '2', '3', '4', '5')
        self.assertIsNone(product.get_key(), None)
