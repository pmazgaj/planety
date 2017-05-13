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
    print("calculating mean")
    return sum(column) / len(column)


def get_sum_for_column(column: list) -> float:
    """Sum up everything in column"""
    return sum(column)


def multiply_two_lists(quantities: list, prices: list) -> list:
    """
    Multiply list by another list
    :return: list with converted values
    """
    quantities = get_parsed_column(quantities)
    prices = get_parsed_column(prices)

    print(quantities)
    print(prices)

    return [a * b for a, b in zip(quantities, prices)]
    # return value * multiplier


def convert_currency(value: float, multiplier: float) -> float:
    """
    Multiply currency (value) by given multiplier
    :return: converted integer number
    """
    column = get_parsed_column(column)

    return value * multiplier
