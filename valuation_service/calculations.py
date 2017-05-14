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


def parse_num(num: str) -> float:
    """Get number from string, if incorrect - return 0"""
    return int(num) if num.isdigit() else 0
