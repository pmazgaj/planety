"""
File for importing csv directly into models.
Currently - for shop and category models.
"""
import csv
import os

__author__ = "Przemek"

PROJECT_PATH = os.path.realpath(os.getcwd())
CSV_PATH = os.path.join(PROJECT_PATH, 'csv')


def get_all_values_for_column(file_all_values: list, column_name: str) -> list:
    """
    Get data for every single column
    :param file_all_values: all elements in file
    :param column_name: name of column to get
    :return:
    """
    column = []
    for element in file_all_values:
        column.append(element.get(column_name, None))
    return column


def convert_currency(value: float, multiplier: float) -> float:
    """
    Multiply currency (value) by given multiplier
    :return: converted integer number
    """
    return value * multiplier


def save_csv_to_file():
    """
    Save results to file top_products
    :return:
    """
    with open(os.path.join(CSV_PATH, 'top_products.csv'), mode='w+') as file:
        file.write('hejka')


def parse_reader(reader: csv.DictReader) -> list:
    """
    Return list of all data sets in file
    :param reader:
    :return:
    """
    return [row for row in reader]


def parse_csv(file: str) -> csv.DictReader:
    """
    Open csv file, return dict for file
    :param file: file, with extension
    :return: dict describing file (e.g. column_name: column}
    """

    with open(os.path.join(CSV_PATH, file)) as file:
        reader = csv.DictReader(file)
        return parse_reader(reader)


def main():
    """
    Handle entire module
    :return:
    """
    currencies = parse_csv('currencies.csv')
    # matches = parse_csv('matchings.csv')
    # data = parse_csv('data.csv')

    currencies_list = get_all_values_for_column(currencies, 'currency')
    ratio_list = get_all_values_for_column(currencies, 'ratio')
    print(currencies_list)
    print(ratio_list)

    # save final results
    save_csv_to_file()


if __name__ == "__main__":
    main()
