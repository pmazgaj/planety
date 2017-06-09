"""
Model for class Product
"""

__author__ = "Przemek"


class Product:
    """Model for product (from csv files)"""

    def __init__(self, prod_id, price, currency, quantity, matching_id):
        self.prod_id = int(prod_id)
        self.price = float(price) if price.lstrip('-'). \
            replace('.', '', 1).isdigit() else 1.0
        self.currency = currency
        self.quantity = float(quantity) if quantity. \
            lstrip('-').replace('.', '', 1).isdigit() else 1.0
        self.matching_id = int(matching_id)
        self.total_price = self.price * self.quantity
        self.converted_total_price = None

    def __str__(self):
        return "id: {} price: {} currency: {} " \
               "quantity: {} matching_id: {}, total_price: {} converted price: {}" \
            .format(self.prod_id, self.price,
                    self.currency, self.quantity,
                    self.matching_id,
                    self.total_price,
                    self.converted_total_price)

    def __cmp__(self, other):
        if hasattr(other, 'total_price'):
            return self.total_price.__cmp__(other.total_price)

    def get_key(self):
        """Get key for user-defined sort"""
        return self.converted_total_price

    def __repr__(self):
        return "{}".format(self.converted_total_price)