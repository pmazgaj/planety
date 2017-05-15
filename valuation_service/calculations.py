"""
Make calculations for value..
"""

__author__ = "Przemek"


def get_parsed_column(column: list) -> list:
    """
    Get column with only float numbers
    :param column: 
    :return: 
    """
    return [parse_num(x) for x in column]


def get_average_value_for_column(column: list) -> float:
    """Return mean for column"""
    column = get_parsed_column(column)
    # print("calculating mean")
    return sum(column) / len(column)


def get_sum_for_column(column: list) -> float:
    """Sum up everything in column"""
    return sum(column)


def parse_num(num: str) -> float:
    """Get number from string, if incorrect - return 0"""
    return float(num) if num.isdigit() else 0.0


def convert_currency(currencies: list, products: list):
    """
    Convert currency to pln by currency and ratio
    :param currencies: list of currencies
    :param products:
    :return:
    """
    for each_currency in currencies:
        for product in products:
            if each_currency.currency == product.currency:
                product.converted_total_price = each_currency.ratio * product.total_price
