"""
Model for class currency
"""

__author__ = "Przemek"


class Currency:
    """Model for currency (from csv files)"""

    def __init__(self, currency, ratio):
        self.currency = currency
        self.ratio = float(ratio) if ratio.lstrip('-').replace('.', '', 1).isdigit() else 1.0

    def __str__(self):
        return "{} {}".format(self.currency, self.ratio)
