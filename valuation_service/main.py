"""
Handle main events for program
"""

from planety.valuation_service.models.matches import Matches
from planety.valuation_service.models.currency import Currency
from planety.valuation_service.models.data import Product
from planety.valuation_service.file_handler import *

__author__ = "Przemek"


def fill_product_object(data_file):
    data_objects = []

    for data in data_file:
        obj_id = data['id']
        price = data['price']
        currency = data['currency']
        quantity = data['quantity']
        matching_id = data['matching_id']

        data_objects.append(Product(obj_id, price, currency, quantity, matching_id))
    return data_objects


def fill_matches_object(matches_file):
    data_objects = []

    for data in matches_file:
        matching_id = data['matching_id']
        top_priced_count = data['top_priced_count']

        data_objects.append(Matches(matching_id, top_priced_count))
    return data_objects


def fill_currency_object(currency_file):
    data_objects = []

    for data in currency_file:
        currency = data['currency']
        ratio = data['ratio']

        data_objects.append(Currency(currency, ratio))
    return data_objects


def convert_currency(currencies: list, products: list):
    for each_currency in currencies:
        for product in products:
            if each_currency.currency == product.currency:
                product.converted_total_price = each_currency.ratio * product.total_price


def get_key(custom):
    return custom.get_key()


def limit_lists(products: list):
    for product in products:
        pass


def compare_products_to_matches(products: list, matches: list):
    value_1 = {}
    value_2 = {}
    value_3 = {}
    dictionary = {}
    products_list = []
    for product in products:
        # print(product)
        for match in matches:
            m_id = match.matching_id
            p_id = product.matching_id

            products_list.append(product)
            if m_id == p_id and m_id == 1:
                limit = match.top_priced_count
                if limit:
                    # print(products_list[-1: limit + 1: -1])
                    value_1.setdefault('valid', products_list[-1: -limit - 1: -1])

            if m_id == p_id and m_id == 2:
                value_2.setdefault('valid', products_list[-1: -limit - 1: -1])
            if m_id == p_id and m_id == 3:
                value_3.setdefault('valid', products_list[-1: -limit - 1: -1])

    print(value_1)
    print(value_2)
    print(value_3)
    return value_3, value_2, value_1
    # return dictionary


def main():
    data_file = parse_csv('data.csv')
    matches_file = parse_csv('matchings.csv')
    currencies_file = parse_csv('currencies.csv')

    products = fill_product_object(data_file)
    matches = fill_matches_object(matches_file)
    currencies = fill_currency_object(currencies_file)

    convert_currency(currencies, products)

    # sorting original copy of list
    products.sort(key=get_key)

    get_matched_lists = compare_products_to_matches(products, matches)
    # print(get_matched_lists)
    # print(products)
    for product in products:
        # print(product)
        ...
        # average =


if __name__ == "__main__":
    main()






















    # a = merge_columns(data_currency, data_price)
    # print(a)
    # print(a)
    # print(data_currency)
    # data_matching_id = get_all_values_for_column(data, 'matching_id')
    # print(data_matching_id)
    # matchings.csv
    # matches = parse_csv('matchings.csv')
    # matches_matching_id = get_all_values_for_column(matches, 'matching_id')
    # matches_top_priced_count = get_all_values_for_column(matches, 'top_priced_count')
    # print(matches)
    # save final results

    # grouped_columns = group_columns_by_param(matches, data)

    # save_csv_to_file()

    # # currency.csv
    # currencies = parse_csv('currencies.csv')
    # currency_currencies = get_all_values_for_column(currencies, 'currency')
    # currency_ratio = get_all_values_for_column(currencies, 'ratio')
    #
    # # data.csv
    # data = parse_csv('data.csv')
    # # print(data)
    # # data_id = get_all_values_for_column(data, 'id')
    # data_quantity = get_all_values_for_column(data, 'quantity')
    # data_price = get_all_values_for_column(data, 'price')
    # data_price = multiply_two_lists(data_quantity, data_price)
    # print(data)
    # print(data_price)
    # # print(data_price * data_quantity)
    # # print(data_price)
    # # print(data_price)
    # data_currency = get_all_values_for_column(data, 'currency')
