"""
Handle *.csv files module
"""
import csv
import os
from planety.definitions import CSV_PATH
from planety.valuation_service.models.matches import Matches
from planety.valuation_service.models.currency import Currency
from planety.valuation_service.models.product import Product

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


def parse_reader(reader: list) -> list:
    """
    Return list of all data sets in file
    :param reader:
    :return:
    """
    return [row for row in reader]


def parse_csv(file: str) -> list:
    """
    Open csv file, return list for file
    :param file: file, with extension
    :return: dict describing file (e.g. column_name: column}
    """

    with open(os.path.join(CSV_PATH, file)) as file:
        reader = csv.DictReader(file)
        return parse_reader(reader)


def fill_product_object(data_file: list) -> list:
    """
    Fill product models for class Product
    :param data_file: file got from data.csv
    :return: list of Product objects
    """
    data_objects = []
    for data in data_file:
        obj_id = data['id']
        price = data['price']
        currency = data['currency']
        quantity = data['quantity']
        matching_id = data['matching_id']

        data_objects.append(Product(obj_id, price, currency, quantity, matching_id))
    return data_objects


def fill_matches_object(matches_file: list) -> list:
    """
    Fill matches model for class Matches
    :param matches_file: file got from matches.csv
    :return: list of Matches objects
    """

    data_objects = []

    for data in matches_file:
        matching_id = data['matching_id']
        top_priced_count = data['top_priced_count']

        data_objects.append(Matches(matching_id, top_priced_count))
    return data_objects


def fill_currency_object(currency_file):
    """
    Fill matches model for class Currency
    :param currency_file: file got from currencies.csv
    :return: list of Currency objects
    """
    data_objects = []

    for data in currency_file:
        currency = data['currency']
        ratio = data['ratio']

        data_objects.append(Currency(currency, ratio))
    return data_objects
