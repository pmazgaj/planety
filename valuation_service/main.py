"""
Handle main events for program
"""

from planety.valuation_service.models.matches import Matches
from planety.valuation_service.models.currency import Currency
from planety.valuation_service.models.data import Product
from planety.valuation_service.file_handler import get_all_values_for_column,\
    parse_csv, save_csv_to_file
from planety.valuation_service.calculations import get_parsed_column

# from planety.definitions import run_py_lint

__author__ = "Przemek"


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


def get_key(custom):
    """Allows to sort by an object property"""
    return custom.get_key()


def create_dict_matching_products(matches_id: list) -> dict:
    """
    Create empty dictionary for matching ID's
    :param matches_id:
    :return:
    """
    max_id = max(matches_id)
    dictionary = {}
    counter = 1
    while counter <= max_id:
        dictionary[counter] = []
        counter += 1
    return dictionary


def compare_products_to_matches(products: list, matches: list, matches_id: list) -> dict:
    """
    Fill the dictionary, according to matching id
    :param products:
    :param matches:
    :param matches_id:
    :return: Dictionary for each matching id from matches.csv
    """
    dict_valid_products = create_dict_matching_products(matches_id)
    for product in products:
        for match in matches:
            m_id = match.matching_id
            p_id = product.matching_id
            if m_id == p_id:
                dict_valid_products[p_id].append(product)

    return dict_valid_products


def get_top_low_for_match(match_ids: dict) -> list:
    """
    Get top elements from dict for each key
    :param match_ids:
    :return:
    """
    for each_elem in match_ids:
        pass
    return list()


def main():
    """Main function to handle everything"""
    # run_py_lint()

    data_file = parse_csv('data.csv')
    matches_file = parse_csv('matchings.csv')
    currencies_file = parse_csv('currencies.csv')

    products = fill_product_object(data_file)
    matches = fill_matches_object(matches_file)
    currencies = fill_currency_object(currencies_file)

    convert_currency(currencies, products)

    # sorting original copy of list
    products.sort(key=get_key)

    matching_id_lists = get_parsed_column(get_all_values_for_column(matches_file, 'matching_id'))

    get_matched_lists = compare_products_to_matches(products, matches, matching_id_lists)

    get_top_low_for_match(get_matched_lists)

    save_csv_to_file()


if __name__ == "__main__":
    main()
