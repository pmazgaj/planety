"""
File for importing csv directly into models.
Currently - for shop and category models.
"""
import csv
import sys
import os
import pprint as pp

__author__ = "Przemek"

PROJECT_PATH = os.path.realpath(os.getcwd())
CSV_PATH = os.path.join(PROJECT_PATH, 'csv')


def convert_currency() -> int:
    """

    :return: converted integer number
    """
    return int


def save_csv():
    """
    Save results to file top_products
    :return:
    """
    with open(os.path.join(CSV_PATH, 'top_products.csv'), mode='w+'):
        print('writing')


def parse_reader(reader: csv.DictReader):
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
        parsed_data = parse_reader(reader)
        return parsed_data


def main():
    """
    Handle entire module
    :return:
    """
    currencies = parse_csv('currencies.csv')
    matches = parse_csv('matchings.csv')
    data = parse_csv('data.csv')

    # currencies = parse_reader(currencies)
    # matches = parse_reader(matches)
    # data = parse_reader(data)

    print(currencies)


if __name__ == "__main__":
    main()
