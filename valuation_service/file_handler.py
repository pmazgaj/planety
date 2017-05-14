"""
Handle *.csv files module
"""
import csv
import os
from planety.definitions import CSV_PATH

__author__ = "Przemek"


def get_all_values_for_column(file_all_values: list, column_header: str) -> list:
    """
    Get data for every single column
    :param file_all_values: all elements in file
    :param column_header: name of column to get
    :return:
    """
    column = []
    for element in file_all_values:
        column.append(element.get(column_header, None))
    return column


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


def parse_csv(file: str) -> list:
    """
    Open csv file, return dict for file
    :param file: file, with extension
    :return: dict describing file (e.g. column_name: column}
    """

    with open(os.path.join(CSV_PATH, file)) as file:
        reader = csv.DictReader(file)
        return parse_reader(reader)





